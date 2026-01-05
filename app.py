from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def get_response(name: str) -> str:
    prompt = PromptTemplate.from_template("Say hello to {name}")
    parser = StrOutputParser()

    chain = prompt | parser
    return chain.invoke({"name": name})
