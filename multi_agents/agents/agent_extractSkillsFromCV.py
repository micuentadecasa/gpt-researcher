from .utils.views import print_agent_output
from .utils.llms import call_model
import json

from mirascope.core import openai, prompt_template
from pydantic import BaseModel

class Skill(BaseModel):
    skill_name: str
    skill_description: str

@openai.call(model="gpt-4o-mini", response_model=list[Skill], json_mode=True)
@prompt_template("""
                 SYSTEM: when answering user questions first output your thought proccess, then reflection on it, and then return the answer
                 USER: List the skills and their descriptions for a {jobDescription}, don't make up anything, list only the skills mentioned, nothing else.""")
def extractSkillsFromJD(jobDescription: str):
    print_agent_output(output="reviewing keypoints..", agent="PUBLISHER")
    ... 

#book = recommend_book("science fiction")
#assert isinstance(book, Book)
#print(f"Title: {book.title}")
#print(f"Author: {book.author}")
