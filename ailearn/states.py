import os
# this is how we create state

#1st way is typed DICT(most usual)
from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int

#2nd way is pydantic approach
#this approach is good at data validation and type checking at runtime

from pydantic import BaseModel, field_validator 

class state(BaseModel):
    topic : str
    score : int
    summary : str = ""


    @field_validator 
    def score_positive(cls, v):
        if v < 0:
            raise ValueError("score must be positive")
        
#3rd way is python dataclass (used very rarely)
from dataclasses import dataclass, field

@dataclass
class State:
    topic : str =""
    summary : str = ""
    messages : list = field(default_factory=list)

    