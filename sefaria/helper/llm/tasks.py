"""
Celery tasks for the LLM server
"""
from typing import List
from celery import shared_task
from sefaria.model.text import Ref
from sefaria.model.topic import Topic
from sefaria.helper.llm.topic_prompt import make_topic_prompt_input


@shared_task
def generate_topic_prompts(lang: str, sefaria_topic: Topic, orefs: List[Ref], contexts: List[str]):
    return make_topic_prompt_input(lang, sefaria_topic, orefs, contexts)


@shared_task
def save_topic_prompts(topic_prompts: List[dict]):
    pass