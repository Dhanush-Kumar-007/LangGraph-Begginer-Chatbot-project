import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

load_dotenv()

class AgentState(TypedDict, total=False):
    question: str
    answer: str

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")
    
llm = ChatGroq(model="llama-3.3-70b-versatile")

def generate(state: AgentState):
    response = llm.invoke(state["question"])
    return {
        "answer": response.content
    }

def check(state: AgentState):
    answer = state.get("answer", "")
    if len(answer.split()) < 20:
        return "retry"
    return "end"

graph = StateGraph(AgentState)

graph.add_node("generate", generate)
graph.add_conditional_edges(
    "generate",
    check,
    {
        "retry": "generate",
        "end": END
    }
)

graph.set_entry_point("generate")

app = graph.compile()

if __name__ == "__main__":
    try:
        result = app.invoke({
            "question": "Explain LangGraph in simple terms"
        })
        print(result.get("answer", "No answer generated"))
    except Exception as e:
        print(f"An error occurred: {e}")
