import dotenv
import os
import sys

dotenv.load_dotenv()


# Load documents
from langchain.document_loaders import PyPDFDirectoryLoader


FILE_PATH = "./documents/"  # Parameter
JOB_DESC = """
New Relic, Senior Machine Learning Engineer
Your opportunity We are looking for a Senior Machine Learning Engineer to join the Applied Intelligence Research Team. The team is responsible for developing novel solutions that are setting a new industry standard for application and system observability. AIOps is an emerging field in the IT operations ecosystem that focuses on augmenting existing operations with machine learning and data science approaches. By Working with huge datasets and modern data analysis frameworks, we are creating new ways to automatically monitor applications, improve the understanding of production incidents, and manage the collective knowledge base of SRE/DevOps teams. What you'll do
Work alongside Data Scientists and Data Engineers to turn machine learning research concepts into scalable production-grade components.
Encourage engineering good practices regarding design and coding.
Design and implement pipelines for large-scale data collection, analysis, and persistence as well as training and serving machine learning-based models.
Collaborate with various engineering teams across the organization, integrating machine learning capabilities into multiple products.This role requires
5+ years of professional experience as a software developer in the industry
Expertise with Python, Kotlin, or similar programming languages
Experience with designing, developing, and testing scalable distributed systems
Experience with message broker systems (e.g. Kafka, RabbitMQ, etc..)
Familiarity with application instrumentation and monitoring practicesBonus points if you have
3+ years of developing production-grade applications in Python
Experience with deploying Machine Learning models in production
Experience with Kubernetes and containers
Familiarity with any of the following concepts/libraries: mlflow, sklearn, tensorflow, kubeflow, argo, seldon
Experience with Spark and distributed computing practices
Experience with AWS
We're looking for bold and passionate people to be a part of our mission to help every engineer do their best work, every day, using data, not opinions, at every stage of the software lifecycle. We'd love to have you apply, even if you don't feel you meet every single requirement.
""".strip()
job_desc_limit = 500

if not os.path.exists(FILE_PATH):
    print("\nPath not found!!!")
    sys.exit(0)

cv_loader = PyPDFDirectoryLoader(FILE_PATH)

# Split documents
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(cv_loader.load())

# Embed and store splits
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# Prompt
from langchain.prompts import PromptTemplate
from src import prompt

rag_prompt = PromptTemplate(
    template=prompt.COVER_LETTER,
    input_variables=["agent_role", "job_desc", "task", "context"],
)

# Generate
# LLM
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

# RAG chain
from langchain.chains import LLMChain

rag_chain = LLMChain(llm=llm, prompt=rag_prompt)
output = rag_chain.run(
    agent_role="Professional cover letter writer",
    job_desc=JOB_DESC,
    task="Help write me a customized cover letter",
    context=retriever,
)
print(output)
