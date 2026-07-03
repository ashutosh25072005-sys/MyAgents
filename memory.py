from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb


load_dotenv()
db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="llama-3.3-70b-versatile"),
        markdown=True,
        add_history_to_context=True
    )

groq_agent = build_agent()

groq_agent.print_response("what is the capital of Australia?")
groq_agent.print_response("what is the best time to visit it?")