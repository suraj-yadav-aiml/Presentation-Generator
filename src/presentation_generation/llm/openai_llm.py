from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
from src.presentation_generation.llm.base_llm import BaseLLMProvider
from typing import Optional



class OpenAILLM(BaseLLMProvider):
    """OpenAI LLM provider implementation."""
    
    def get_llm_model(self) -> Optional[BaseChatModel]:
        """Initialize and return an OpenAI LLM model."""
        try:
            # Clear previous error messages
            self.error_messages = []

            openai_api_key = self._get_api_key(api_key_name="OPENAI_API_KEY")

            if self._validate_requirements(
                api_key=openai_api_key,
                model=self.model_name,
                api_key_name="OPENAI_API_KEY",
                provider_name="OpenAI"
            ):
                try:
                    self.llm = ChatOpenAI(
                        api_key=openai_api_key,
                        model=self.model_name,
                        max_tokens=self.max_tokens,
                        temperature=self.temperature
                    )
                except Exception:
                    # Fallback with default parameters
                    self.llm = ChatOpenAI(
                        api_key=openai_api_key,
                        model=self.model_name,
                    )
                return self.llm
            else:
                self.display_errors()
                return None
                                           
        except Exception as e:
            self.error_messages.append(f"Error initializing OpenAI LLM: {str(e)}")
            self.display_errors()
            return None