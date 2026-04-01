import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Clé API Groq
os.environ["GROQ_API_KEY"] = "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"

# Initialiser le modèle
chat_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
)

# Message système (personnalité pirate)
system_message = SystemMessage(
    content="You are a friendly pirate who loves to share knowledge. Always respond in pirate speech, use pirate slang, and include plenty of nautical references. Add relevant emojis throughout your responses. Arr! ☠️🏴‍☠️"
)

# Question
question = "What are the 7 wonders of the world?"

messages = [
    system_message,
    HumanMessage(content=question)
]

# Obtenir la réponse
response = chat_model.invoke(messages)

print("\nQuestion:", question)
print("\nPirate Response:")
print(response.content)