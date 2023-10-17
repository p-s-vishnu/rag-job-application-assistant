from . import prompt, llm, retriever, utils


def generate_cover_letter(filepath, job_desc):
    retriever_obj = retriever.create(filepath)
    utils.stream(
        llm.generate_response(
            retriever=retriever_obj,
            prompt=prompt.CHAT_PROMPT,
            job_desc=job_desc,
            mode="cover_letter",
        )
    )


def consult_agent(filepath, task, job_desc):
    retriever_obj = retriever.create(filepath)
    utils.stream(
        llm.generate_response(
            retriever=retriever_obj,
            prompt=prompt.CHAT_PROMPT,
            job_desc=job_desc,
            mode="consult",
            task=task,
        )
    )
