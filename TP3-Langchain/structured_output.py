import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

os.environ["GROQ_API_KEY"] = "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"

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=500,
)

# Modèle de sortie structurée
class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")

# Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Template
prompt_template_text = """
Response with a movie recommendation based on the query:
{format_instructions}
{query}
"""

prompt_template = PromptTemplate(
    template=prompt_template_text,
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Chaîne LCEL
chain = prompt_template | llm | parser
response = chain.invoke({"query": "A 90s movie with Nicolas Cage."})
print(response)