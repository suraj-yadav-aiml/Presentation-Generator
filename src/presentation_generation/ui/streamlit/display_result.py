
import streamlit as st
import traceback
import time
from datetime import datetime
from typing import Dict, Any, Optional


class DisplayResultStreamlit:
    
    def __init__(self, graph, user_input: Dict[str, Any]):

        self.graph = graph
        self.user_input = user_input 
        self.start_time = None
    
    def display_result_on_ui(self):
        try:
            with st.chat_message('user', avatar="👤"):

                st.markdown(f"**Presentation Topic:** {self.user_input['topic']}")
                
                with st.expander("Request Details", expanded=False):
                    if 'audience' in self.user_input and self.user_input['audience']:
                        st.markdown(f"**Audience:** {self.user_input['audience']}")
                    if 'tone' in self.user_input and self.user_input['tone']:
                        st.markdown(f"**Tone:** {self.user_input['tone']}")
                    if 'no_of_slides' in self.user_input:
                        st.markdown(f"**Slides:** {self.user_input['no_of_slides']}")
                    if 'presentation_style' in self.user_input:
                        st.markdown(f"**Style:** {self.user_input['presentation_style']}")
                    if 'presentation_purpose' in self.user_input:
                        st.markdown(f"**Purpose:** {self.user_input['presentation_purpose']}")

            
            self.start_time = time.time()
            
            with st.spinner(text="Generating presentation..."):

                presentation = self.graph.invoke(
                    input={
                        "topic": self.user_input.get('topic', ''),
                        "audience": self.user_input.get('audience', ''),
                        "tone": self.user_input.get('tone', ''),
                        "no_of_slides": self.user_input.get('no_of_slides', 10),
                        "presentation_style": self.user_input.get('presentation_style', ''),
                        "presentation_purpose": self.user_input.get('presentation_purpose', ''),
                        "special_instructions": self.user_input.get('special_instructions', '')
                    }
                )
            

            elapsed_time = time.time() - self.start_time
            st.caption(f"Generation completed in {elapsed_time:.2f} seconds")

            if 'final_presentation' in presentation:
                presentation_content = presentation.get("final_presentation")
                
                with st.chat_message('assistant', avatar="🤖"):

                    topic = self.user_input.get('topic',"Presentation")
                    file_name = datetime.now().strftime("%Y%m%d_%H%M%S")
                    st.download_button(
                        label="📥 Download Presentation",
                        data=presentation_content,
                        file_name=f"{topic}_{file_name}.md",
                        mime="text/markdown",
                    )

                    with st.expander("Generated Presentation", expanded=True):
                        st.markdown(presentation_content)

            else:
                st.warning("No presentation content was generated. Please try again.")

        except Exception as e:
            error_msg = f"Error generating presentation: {str(error)}"
            st.error(error_msg)
            
            with st.expander("Error Details", expanded=False):
                st.code(traceback.format_exc(), language="python")
            
            return None
    