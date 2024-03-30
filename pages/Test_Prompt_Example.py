import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

# Uncomment to use locally

load_dotenv('.env')

llm_url = os.environ.get("LLM_URL")
llm_model = os.environ.get("LLM_MODEL")
openai_api_key = os.environ.get("OPENAI_API_KEY")

llm_chat = ChatOpenAI(
    model=llm_model,
    base_url=llm_url,
    openai_api_key=openai_api_key,
    streaming=True
)

st.set_page_config(layout="wide")

def query_llm(input_prompt):
    """
    Send a query to the LLM using LangChain and get a response.

    Parameters:
    - input_prompt (str): The user's query.

    Returns:
    - str: The response from the LLM.
    """
    # Ensure the input is formatted as expected by the ChatOpenAI class.
    formatted_input = [{
        "role": "user",
        "content": input_prompt
    }]

    # Adjust the call to match the expected input format.
    return llm_chat.stream(formatted_input)

# Streamlit UI setup
st.title("Multi-GPU Testing Chat 100 Tokens")

user_prompt = "Can you write me a Github action that will echo hello " \
             "then build a docker container from the Dockerfile called " \
             "testing-docker and report the status in the log. If that step " \
             "is successful then it should be able to login to dockerhub, " \
             "then push docker image with a tag"


# 123 Token, much longer response
# user_prompt = "We need to write a set of Kubernetes manifest to deploy an " \
#              "application to a cluster. This will need to include a manifest" \
#              "to deploy an ingress object using an alb controller for AWS, " \
#              "a secrets manifest for using external secrets to store application" \
#              "config in AWS secrets manager. We will need to have a manifest for a" \
#              "kubernetes service. Then a manifest for a kubernetes deployment in " \
#              "code examples"


st.write(user_prompt)

# Show disabled message for hosted
st.write("Chat Disabled for Web App")

# Button to send the message
# if st.button("Send"):
#     if user_prompt:
#         # Display user's message
#         st.write(f"You: {user_prompt}")

#         # Get and display the LLM's response
#         st.write_stream(query_llm(user_prompt))
#     else:
#         st.warning("Please enter a message to send.")
