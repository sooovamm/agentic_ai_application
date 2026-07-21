import os
from typing import TypedDict

class pipelinestate(TypedDict):
    raw_input : str
    edited_text : str
    script_text : str
    final_output : str
    

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def editor_node(state :pipelinestate) -> dict:
    """stage 1: cleans up grammar, removes typos, and refines the tone."""

    prompt = (
        "you are an expert copyeditor. clean up the following raw text."
        "fix any grammatical errors, spelling mistakes, and smooth out the transition flow"
        "while keeping the core message intact. return only the edited text. \n\n"
        f"Text:\n{state['raw_input']}"
    )
    response = llm.invoke(prompt)
    return {"edited_text" : response.content.strip()}

def scriptwriter_node(state :pipelinestate) -> dict:
    """stage 2: Formats the clean text into an engaging video script style."""
    print("\n--- [stage 2] Executing Scriptwriter Node ---")

    prompt = (
        "you are a charismatic youtube content creator. take this edited text and transform "
        "it into a highly engaging, punchy, conversational video script hook. Make it sound "
        "like a real person speaking passionately. return only the script content. \n\n"
        f"Edited Text:\n{state['edited_text']}"
    )
    response = llm.invoke(prompt)
    return {"script_text" : response.content.strip()} 

def translator_node(state: pipelinestate) -> dict:
    """stage 3: Translates the script into natural flowing Hinglish."""
    print("\n--- [stage 3] Executing Hinglish translator Node ---")

    prompt = (
        "you are an expert content loaclizer for the Indian market. Take the following script"
        "and convert it into natural, flowing 'hinglish'. Do not simply translate it sentence-by-sentence"
        "or repeat information. alternating comfortably between hindi and english phrases just like"
        "an inr=tellectual tech educator would speak naturally on a live stream. keep the energy high and"
        "return only the final Hinglish text. \n\n"
        f"Edited Text:\n{state['script_text']}"
    )
    response = llm.invoke(prompt)
    return {"final_output" : response.content.strip()} 

#now we create the edges as the nodes and states are done to create the graph

from langgraph .graph import StateGraph, START, END

graph= StateGraph(pipelinestate)

#add the nodes in our graph 

graph.add_node("editor",editor_node)
graph.add_node("scriptwriter",scriptwriter_node)
graph.add_node("translator",translator_node)

#add edges in sequential

graph.add_edge(START,"editor")
graph.add_edge('editor',"scriptwriter")
graph.add_edge('scriptwriter',"translator")
graph.add_edge('translator',END)

#compile the graph
app = graph.compile()

result = app.invoke({
    "raw_input" : "AI agents are the future of tech. they can think, plan, and act on their own."
})

print("your result are :- \n\n")
print(result['final_output'])