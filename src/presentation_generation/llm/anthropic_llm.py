from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from src.presentation_generation.llm.base_llm import BaseLLMProvider
from typing import Optional


class AnthropicLLM(BaseLLMProvider):
    """Anthropic LLM provider implementation."""

    def get_llm_model(self) -> Optional[BaseChatModel]:
        """Initialize and return an Anthropic LLM model."""
        try:
            # Clear previous error messages
            self.error_messages = []

            anthropic_api_key = self._get_api_key(api_key_name="ANTHROPIC_API_KEY")

            if self._validate_requirements(
                api_key=anthropic_api_key,
                model=self.model_name,
                api_key_name="ANTHROPIC_API_KEY",
                provider_name="Anthropic"
            ):
                self.llm = ChatAnthropic(
                    api_key=anthropic_api_key,
                    model=self.model_name,
                    max_tokens=8000,
                    temperature=0.7
                )
                return self.llm
            else:
                self.display_errors()
                return None
                                           
        except Exception as e:
            self.error_messages.append(f"Error initializing Anthropic LLM: {str(e)}")
            self.display_errors()
            return None