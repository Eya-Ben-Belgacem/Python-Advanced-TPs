import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

os.environ["GROQ_API_KEY"] = "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"

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=500,
)

# Template de prompt
prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)

# Chaîne avec l'opérateur pipe
chain = prompt_template | llm

response = chain.invoke({
    "n": 5,
    "cuisine": "Italian"
})

print("\nPrompt: List 5 cooking/meal titles for Italian cuisine")
print("\nResponse:")
print(response.content)