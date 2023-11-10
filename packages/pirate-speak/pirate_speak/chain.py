from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Translate user input into pirate speak",
        ),
        ("human", "{text}"),
    ]
)
_model = ChatOpenAI(model='gpt-3.5-turbo', api_key=OPEN_AI_API_KEY)

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
