# expert Job application consultant, professional cover letter writer
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.load.load import loads


TEMPLATE = """
You are a {agent_role}. 

Please use the information from the provided CV/Resume to craft tailored answer in response to the following job description. 
Follow these guidelines:
1. If you lack relevant information, you may state that you don't have the specific details.
2. Select experiences from the CV/Resume that best align with the job description.
3. Keep your response concise and formal in a first-person style.

**Job Description:**
{job_desc}

**Task:**
{task}

**CV/Resume Context:**
{context}

Answer:
"""
CHAT_PROMPT = ChatPromptTemplate.from_template(TEMPLATE)
