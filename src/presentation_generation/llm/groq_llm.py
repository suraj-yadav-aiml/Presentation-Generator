from langchain_groq import ChatGroq
from langchain_core.language_models.chat_models import BaseChatModel
from src.presentation_generation.llm.base_llm import BaseLLMProvider
from typing import Optional




class GroqLLM(BaseLLMProvider):
    """Groq LLM provider implementation."""

    def get_llm_model(self) -> Optional[BaseChatModel]:
        """Initialize and return a Groq LLM model."""
        try:
            self.error_messages = [] 

            groq_api_key = self._get_api_key(api_key_name="GROQ_API_KEY")

            if self._validate_requirements(
                api_key=groq_api_key,
                model=self.model_name,
                api_key_name="GROQ_API_KEY",
                provider_name="Groq"
            ):
                self.llm = ChatGroq(
                    api_key=groq_api_key,
                    model=self.model_name,
                    max_tokens=10_000,
                    temperature=0.7
                )
                
                return self.llm
            else:
                self.display_errors()
                return None
            
        except Exception as e:
            self.error_messages.append(f"Error initializing Groq LLM: {str(e)}")
            self.display_errors()
            return None
