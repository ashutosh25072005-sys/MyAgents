
#used Agno framework
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[
            YFinanceTools(
                enable_stock_price=True,
                enable_analyst_recommendations=True,
                enable_company_info=True,
            )
        ],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."]
    )

groq_agent = build_agent()

groq_agent.print_response("Share the NVDA stock price and analyst recommendations?")