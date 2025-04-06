import os
import streamlit as st
from typing import Dict, List, Optional, Type, Union
from abc import ABC, abstractmethod
from langchain_core.language_models.chat_models import BaseChatModel


class BaseLLMProvider(ABC):
    """Base class for all LLM providers."""
    
    def __init__(self, model_name: str, api_key: Optional[str] = None, 
                 temperature: float = 0.7, max_tokens: int = 2048):
        """
        Initialize the LLM provider.
        
        Args:
            model_name: Name of the model to use
            api_key: API key for the provider (optional - can be retrieved from env or session)
            temperature: Temperature parameter for controlling randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
        """
        self.model_name = model_name
        self.api_key = api_key
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.llm = None
        self.error_messages: List[str] = []
    
    def _get_api_key(self, api_key_name: str) -> str:
        """
        Get API key from provided value, environment, or session state.
        
        Args:
            api_key_name: Name of the API key environment variable
            
        Returns:
            API key if found, empty string otherwise
        """
        return self.api_key or os.getenv(api_key_name) or st.session_state.get(api_key_name, "")
    
    def _validate_requirements(self, api_key: str, model: str, api_key_name: str, provider_name: str) -> bool:
        """
        Validate that required parameters are provided.
        
        Args:
            api_key: API key to validate
            model: Model name to validate
            api_key_name: Name of the API key for error messages
            provider_name: Name of the provider for error messages
            
        Returns:
            True if all requirements are valid, False otherwise
        """
        is_valid = True

        if not api_key:
            is_valid = False
            self.error_messages.append(f"Please provide a {api_key_name} API key.")
        
        if not model:
            is_valid = False
            self.error_messages.append(f"Please provide a {provider_name} model name.")
        
        return is_valid
    
    def display_errors(self) -> None:
        """Display all error messages using Streamlit."""
        for message in self.error_messages:
            st.error(message)
    
    @abstractmethod
    def get_llm_model(self) -> Optional[BaseChatModel]:
        """
        Initialize and return the appropriate LLM model.
        
        Returns:
            Configured LLM model or None if initialization fails
        """
        pass