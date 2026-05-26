import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

def load_llm(config: str):
    load_dotenv()
    provider = os.getenv("LLM_PROVIDER")
    
    if provider == 'openai':
        return ChatOpenAI(
            model=config['llm']['openai_model'],
            temperature=config['llm']['temperature']
        )
    elif provider == 'gemini':
        return ChatGoogleGenerativeAI(
            model=config['llm']['gemini_model'],
            temperature=config['llm']['temperature']
        )
    else:
        raise ValueError(f"Invalid LLM Provider. Please provide appropriate LLM_PROVIDER: {provider}")