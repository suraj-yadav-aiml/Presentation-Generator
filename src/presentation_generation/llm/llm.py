from langchain_core.language_models.chat_models import BaseChatModel
from typing import Dict, Optional, Type
import streamlit as st
from src.presentation_generation.llm.base_llm import BaseLLMProvider
from src.presentation_generation.llm.groq_llm import GroqLLM
from src.presentation_generation.llm.openai_llm import OpenAILLM
from src.presentation_generation.llm.anthropic_llm import AnthropicLLM



def get_llm(
    provider: str, 
    model_name: str, 
    api_key: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 2048
) -> Optional[BaseChatModel]:
    """
    Get an LLM model instance with simplified interface.
    
    Args:
        provider: LLM provider name 
        model_name: Name of the model to use
        api_key: Optional API key (will use env vars or session state if not provided)
        temperature: Temperature parameter for controlling randomness (0.0 to 1.0)
        max_tokens: Maximum number of tokens to generate
        
    Returns:
        Configured LLM model instance or None if initialization fails
    """
    llm_providers: Dict[str, Type[BaseLLMProvider]] = {
        "Groq": GroqLLM,
        "OpenAI": OpenAILLM,
        "Anthropic": AnthropicLLM
    }
    
    llm_class = llm_providers.get(provider)
    
    if llm_class:
        try:
            llm_provider = llm_class(
                model_name=model_name, 
                api_key=api_key,
                temperature=temperature,
                max_tokens=max_tokens
            )
            llm_model = llm_provider.get_llm_model()
            
            if llm_model:
                return llm_model
            else:
                return None
                
        except Exception as e:
            error_msg = f"Error initializing {provider} LLM: {str(e)}"
            st.error(error_msg)
            return None
    else:
        supported_providers = ', '.join(llm_providers.keys())
        error_msg = f"Unsupported LLM provider: {provider}"
        
        st.error(error_msg)
        st.info(f"Supported providers: {supported_providers}")
        return None