import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import streamlit as st
import pandas as pd
#from pandasai import smart_dataframe
from pandasai.llm import azure_openai

# Load the environment variables
load_dotenv()

# Load the Azure OpenAI credentials from the environment variables
aoai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
aoai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
aoai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
aoai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint= 'https://techexcel201108.openai.azure.com/',
    api_key = 'FuEMilNR0SJVDQp97bQNEscuWijJA07JzSSTXOnwvatjpPr2PTSHJQQJ99AKACYeBjFXJ3w3AAABACOGfV3n',
    api_version = "2024-02-01")
'''
# Create a completion prompt to set the behavior aimed using the Azure OpenAI client
completion = client.chat.completions.create(
    model= "gpt-4o", #aoai_deployment_name,
    messages=[
        {
            "role": "user", 
            "content": "What should I know about generating structured output data from latest OpenAI GPT-4o available?"
        }
    ]
)

# Prints only the Natural Language response answer from Azure OpenAI
print("Direct Answer to the question: ", completion.choices[0].message.content.strip())

'''

# Creates a page title for the Streamlit app
st.write("# Chat with your Amazon 5-Start Rating Customer product Review")

df = pd.read_json('source_data/All_Beauty.jsonl', lines=True)

# Displays the first 5 rows of the data set
st.write("## Original Amazon 5-Star Rating Dataset Preview:")
with st.expander ("Data preview: "):
    st.write("Original data has columns x rows as following:" ,df.shape)
    st.write(df.head(100))
'''
pandas_ai = PandasAI(client)

query = st.text_input("Ask a question about the dataset:")
st.write("You entered:", query)

if query:
    response = pandas_ai(df, query)
    st.write("Response:", response)

'''
