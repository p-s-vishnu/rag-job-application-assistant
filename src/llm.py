from langchain.chat_models import ChatOpenAI
from operator import itemgetter
from langchain.schema.output_parser import StrOutputParser
import dotenv

dotenv.load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", 
                 temperature=0, 
                 streaming=True)


def generate_response(
    retriever,
    job_desc,
    prompt,
    mode="cover_letter",
    task=None,
):
    if mode == "cover_letter":
        agent_role = "Professional cover letter writer"
        task = "Help write me a customized cover letter"
    elif mode == "consult":
        agent_role = "Job Application Consultant"
        task = "How to answer -> " + task

    rag_chain = (
        {
            # retrieving job description specific passages from the CV
            "context": itemgetter("job_desc") | retriever,
            "task": itemgetter("task"),
            "agent_role": itemgetter("agent_role"),
            "job_desc": itemgetter("job_desc"),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain.invoke(
        {"task": task, "agent_role": agent_role,
         "job_desc": job_desc}
    )
