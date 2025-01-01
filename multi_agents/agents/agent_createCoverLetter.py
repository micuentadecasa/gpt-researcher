from .utils.views import print_agent_output
from .utils.llms import call_model
import json

from mirascope.core import openai, prompt_template
from pydantic import BaseModel

class Skill(BaseModel):
    skill_name: str
    skill_description: str

class CoverLetter(BaseModel):
    coverLetter: str

@openai.call(model="gpt-4o-mini", response_model=CoverLetter, json_mode=True)
@prompt_template("""
                 SYSTEM: when answering user questions first output your thought proccess, then reflection on it, and then return the answer
                 USER: Create a cover letter using the curriculum data from {curriculum} and the skills required in {skills}, don't make up anything, , nothing else.
                  I'd like you to help me write a cover letter that consists of three paragraphs and follows this structure. In the first paragraph, highlight details about the company and give specific reasons as to why I'm interested in joining it. 
                 Use the next paragraph to highlight any of my relevant skills, experiences, or accomplishments that align with the job, using examples of my projects related with the skills. The third and final paragraph should once again highlight why I'm a good fit for the company culture and role. Ensure that the cover letter uses professional language and tone and follows industry best practice examples. Make sure that it's not longer than three paragraphs
                 """)
def createCL(curriculum: list[str], skills: list[Skill]):
    print_agent_output(output="creating coverletter..", agent="PUBLISHER")
    ... 

#book = recommend_book("science fiction")
#assert isinstance(book, Book)
#print(f"Title: {book.title}")
#print(f"Author: {book.author}")
