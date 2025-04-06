import streamlit as st
import os
from src.presentation_generation.ui.uiconfigfile import Config


class StreamlitUILoader:
    def __init__(self):
        self.config = Config()
        self.user_input = {}
    
    def _validate_api_key(self, api_key: str, service: str, reference_link: str) -> None:
        """
        Validate and display warning for API keys.
        
        Args:
            api_key (str): API key to validate
            service (str): Name of the service
            reference_link (str): Link for obtaining API key
        """
        if not api_key:
            st.warning(f"⚠️ Please enter your {service} API key to proceed. Don't have one? Refer: {reference_link}")
    
    def _setup_groq_configuration(self) -> None:
        """Set up Groq LLM configuration in the sidebar."""
        st.sidebar.subheader("Groq Configuration")
        
        groq_model_options = self.config.get_groq_model_options()
        self.user_input['model_name'] = st.sidebar.selectbox(
            label="Select Groq Model", 
            options=groq_model_options,
            help="Choose a Groq model for inference"
        )

        groq_api_key = st.sidebar.text_input(
            label="GROQ API KEY", 
            type='password',
            help="Enter your Groq API key"
        )
        self.user_input['api_key'] = groq_api_key
        st.session_state['GROQ_API_KEY'] = groq_api_key
        os.environ['GROQ_API_KEY'] = groq_api_key  

        self._validate_api_key(
            groq_api_key, 
            "GROQ", 
            "https://console.groq.com/keys"
        )
    
    def _setup_openai_configuration(self) -> None:
        """Set up OpenAI LLM configuration in the sidebar."""
        st.sidebar.subheader("OpenAI Configuration")
        
        openai_model_options = self.config.get_openai_model_options()
        self.user_input['model_name'] = st.sidebar.selectbox(
            label="Select OpenAI Model",
            options=openai_model_options,
            help="Choose an OpenAI model"
        )

        openai_api_key = st.sidebar.text_input(
            label="OPENAI API KEY", 
            type='password',
            help="Enter your OpenAI API key"
        )
        self.user_input['api_key'] = openai_api_key
        st.session_state['OPENAI_API_KEY'] = openai_api_key
        os.environ['OPENAI_API_KEY'] = openai_api_key

        self._validate_api_key(
            openai_api_key, 
            "OpenAI", 
            "https://platform.openai.com/settings/organization/api-keys"
        )
    
    def _setup_anthropic_configuration(self) -> None:
        """Set up Anthropic LLM configuration in the sidebar."""
        st.sidebar.subheader("Anthropic Configuration")
        
        anthropic_model_options = self.config.get_anthropic_model_options()
        self.user_input['model_name'] = st.sidebar.selectbox(
            label="Select Anthropic Model",
            options=anthropic_model_options,
            help="Choose an Anthropic Claude model"
        )

        anthropic_api_key = st.sidebar.text_input(
            label="ANTHROPIC API KEY", 
            type='password',
            help="Enter your Anthropic API key"
        )
        self.user_input['api_key'] = anthropic_api_key
        st.session_state['ANTHROPIC_API_KEY'] = anthropic_api_key
        os.environ['ANTHROPIC_API_KEY'] = anthropic_api_key

        self._validate_api_key(
           anthropic_api_key, 
            "Anthropic", 
            "https://console.anthropic.com/settings/keys"
        )
    
    def load_streamlit_ui(self) -> dict:
        page_title = self.config.get_page_title()
        st.set_page_config(page_title="🤖 " + page_title, layout="wide")
        st.header("🤖 " + page_title)
    

        # Side bar
        with st.sidebar:

            st.title("Model Configuration")

            llm_options = self.config.get_llm_options()
            self.user_input['llm_provider'] = st.selectbox(
                label="Select LLM Provider", 
                options=llm_options,
                help="Choose the AI provider you want to use"
            )

            if self.user_input['llm_provider'] == "Groq":
                self._setup_groq_configuration()
            elif self.user_input['llm_provider'] == "OpenAI":
                self._setup_openai_configuration()
            elif self.user_input['llm_provider'] == "Anthropic":
                self._setup_anthropic_configuration()


            with st.expander("Model Parameters", expanded=False):

                self.user_input['model_temperature'] = st.slider(
                    "Temperature", 
                    min_value=0.0, 
                    max_value=1.0, 
                    value=0.7, 
                    step=0.1,
                    help="Lower for more deterministic responses, higher for more creative ones"
                )

                
                self.user_input['model_max_tokens'] = st.number_input(
                    "Max tokens",
                    value=2048, 
                    step=1024, 
                    min_value=256,
                    help="Maximum length of generated text"
                )

        
        # Main Page

        self.user_input['topic'] = st.text_input(
            "Presentation Topic",
            placeholder="E.g., Quarterly Sales Update, Project Proposal, Industry Trends Analysis"
        )

        col1, col2 = st.columns(2)

        with col1:
            audience_options = [
                "Executive Leadership",
                "Team Members",
                "Board of Directors",
                "Investors",
                "Clients/Customers",
                "General Public",
                "Technical Experts",
                "Sales Team",
                "New Employees",
                "Stakeholders",
                "Conference Attendees",
                "Students",
                "Custom (specify below)"
            ]
            
            self.user_input['audience'] = st.selectbox(
                "Target Audience",
                options=audience_options,
                index=0,
                help="Select your target audience or choose 'Custom' to specify your own"
            )
            
            if self.user_input['audience'] == "Custom (specify below)":
                self.user_input['audience'] = st.text_input(
                    "Specify Custom Audience",
                    placeholder="E.g., Product managers, Remote workers, Industry partners"
                )

        with col2:
            tone_options = [
                "Professional",
                "Informative",
                "Persuasive",
                "Analytical",
                "Motivational",
                "Educational",
                "Formal",
                "Conversational",
                "Authoritative",
                "Enthusiastic",
                "Technical",
                "Simplified",
                "Custom (specify below)"
            ]
            
            self.user_input['tone'] = st.selectbox(
                "Presentation Tone",
                options=tone_options,
                index=0,
                help="Choose the tone for your presentation"
            )
            
            if self.user_input['tone'] == "Custom (specify below)":
                self.user_input['tone'] = st.text_input(
                    "Specify Custom Tone",
                    placeholder="E.g., Inspirational, Story-driven, Data-focused"
                )

        with st.expander("Presentation Details", expanded=True):
            self.user_input['no_of_slides'] = st.slider(
                    "Number of Slides",
                    min_value=5,
                    max_value=30,
                    value=10,
                    step=1,
                    help="Select the approximate number of slides for your presentation"
                )

            col3, col4 = st.columns(2)
            
            with col3:
                
                self.user_input['presentation_style'] = st.selectbox(
                    "Presentation Style",
                    options=[
                        "Business",
                        "Educational",
                        "Sales Pitch",
                        "Project Status",
                        "Research",
                        "Workshop",
                        "Conference",
                        "Training"
                    ],
                    help="Select the overall style of presentation"
                )
            
            with col4:
                
                self.user_input['presentation_purpose'] = st.selectbox(
                    "Presentation Purpose",
                    options=[
                        "Inform/Educate",
                        "Persuade/Sell",
                        "Report Results",
                        "Share Updates",
                        "Train/Teach",
                        "Motivate/Inspire"
                    ],
                    help="Select the main purpose of your presentation"
                )
        
        self.user_input['special_instructions'] = st.text_area(
            "Special Instructions (Optional)",
            placeholder="Any specific points you'd like to include, brand guidelines to follow, or other requirements",
            height=100
        )
        

        return self.user_input
        
            
