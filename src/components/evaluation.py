from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# ===========================================================
# TONE CHAIN
# ===========================================================
class ToneEvaluation(BaseModel):
    score: int = Field(description="Score between 1 and 5")
    reasoning: str = Field(description="Explanation of the score")

def get_tone_chain(llm):
    tone_parser = PydanticOutputParser(pydantic_object=ToneEvaluation)

    tone_prompt = PromptTemplate(
        template="""
        You are a QA evaluator for customer support calls.
        
        Evaluate the agent's tone and empathy in the following transcript.
        
        Consider:
        - Did the agent acknowledge the customer's issue?
        - Was the tone polite and professional?
        - Did the agent show empathy?
        
        Transcript:
        {transcript}
        
        {format_instructions}
        """,
        input_variables=["transcript"],
        partial_variables={
            "format_instructions": tone_parser.get_format_instructions()
        }
    )

    tone_chain = tone_prompt | llm | tone_parser
    return tone_chain

# ===========================================================
# RESOLUTION CHAIN
# ===========================================================
class ResolutionEvaluation(BaseModel):
    score: int = Field(description="Score between 1 and 5")
    reasoning: str = Field(description="Explanation of the score")

def get_resolution_chain(llm):
    
    resolution_parser = PydanticOutputParser(pydantic_object=ResolutionEvaluation)

    resolution_prompt = PromptTemplate(
        template="""
        You are a QA evaluator for customer support calls.
        
        Evaluate the resolution quality of the agent.
        
        Consider:
        - Did the agent fully resolve the customer's issue?
        - Were next steps clearly communicated?
        - Did the agent confirm resolution before ending?
        
        Transcript:
        {transcript}
        
        {format_instructions}
        """,
        input_variables=["transcript"],
        partial_variables={
            "format_instructions": resolution_parser.get_format_instructions()
        }
    )

    resolution_chain = resolution_prompt | llm | resolution_parser
    return resolution_chain

# ===========================================================
# KNOWLEDGE CHAIN
# ===========================================================
class KnowledgeEvaluation(BaseModel):
    score: int = Field(description="Score between 1 and 5")
    reasoning: str = Field(description="Explanation of the score")

def get_knowledge_chain(llm):
    
    knowledge_parser = PydanticOutputParser(pydantic_object=KnowledgeEvaluation)

    knowledge_prompt = PromptTemplate(
        template="""
        You are a QA evaluator for customer support calls.
        
        Evaluate the agent's knowledge accuracy and clarity.
        
        Consider:
        - Did the agent provide correct and relevant information?
        - Was the explanation clear and easy to understand?
        - Did the agent avoid vague or misleading statements?
        
        IMPORTANT:
        - If the transcript does not contain enough information, give a moderate score (2 or 3) and explain what is missing.
        Transcript:
        {transcript}
        
        {format_instructions}
        """,
        input_variables=["transcript"],
        partial_variables={
            "format_instructions": knowledge_parser.get_format_instructions()
        }
    )

    knowledge_chain = knowledge_prompt | llm | knowledge_parser
    return knowledge_chain
