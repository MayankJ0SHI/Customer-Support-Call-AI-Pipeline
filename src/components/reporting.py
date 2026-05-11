from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

#Final Report Schema
class FinalReportSchema(BaseModel):
    summary: str = Field(description="Overall evaluation summary")
    recommendation: list[str] = Field(description="List of actionable improvements")

def get_final_reporting_chain(llm):
    final_parser = PydanticOutputParser(pydantic_object=FinalReportSchema)

    final_prompt = PromptTemplate(
        template="""
        You are a QA manager reviewing customer support calls.
        
        Based on the evaluation results below, generate:
        1. A concise summary of the agent's performance
        2. A list of actionable recommendations for improvement
        
        Evaluation Data:
        {evaluation_output}
        
        IMPORTANT:
        - Be specfic and practical
        - Do not repeat scores
        - Focus on improvement
        
        {format_instructions}
        """,
        input_variables=["evaluation_output"],
        partial_variables={
            "format_instructions": final_parser.get_format_instructions()
        }
    )

    final_chain = final_prompt | llm | final_parser
    return final_chain