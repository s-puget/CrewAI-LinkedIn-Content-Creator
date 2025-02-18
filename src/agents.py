from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, FileReadTool
from datetime import date
from dotenv import load_dotenv

load_dotenv()
current_date = date.today()

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
topics_read_tool = FileReadTool(file_path="./covered_topics.txt")

agent_researcher = Agent(
    role="Hot Tech and AI News Topics Researcher",
    goal="Finds and ranks trending topics in AI and Technology based on the latest news.",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=f"""
        You are a skilled researcher specializing in AI and tech news. Your job is to find 
        the most relevant and up-to-date topics trending in AI and technology. The news must be 
        current, focusing on groundbreaking stories and trends from today ({current_date}) or the past few days.
    """,
    allow_delegation=False
)

agent_topic_selector = Agent(
    role="Topic Selection Strategist",
    goal="Selects the most relevant AI topic while avoiding repetition.",
    tools=[topics_read_tool],
    verbose=True,
    backstory=f"""
        You are an expert in identifying impactful AI topics. Your primary focus is to ensure 
        the topics chosen are up-to-date and aligned with the latest developments, especially from today ({current_date}).
    """,
    allow_delegation=False
)

agent_writer = Agent(
    role="LinkedIn Content Creator",
    goal="Crafts engaging and professional LinkedIn posts based on trending tech topics.",
    verbose=True,
    tools=[search_tool, scrape_tool],
    backstory=f"""
        You create concise, engaging LinkedIn posts on the latest tech topics. Your tone is 
        professional yet conversational, incorporating emojis where appropriate. Today is {current_date}.
    """,
    allow_delegation=False
)

agent_fact_checker = Agent(
    role="AI Fact Checker",
    goal="Ensure the accuracy and credibility of AI-generated LinkedIn posts.",
    verbose=True,
    tools=[search_tool, scrape_tool],
    backstory="""
        You verify LinkedIn posts for factual accuracy and credibility. You cross-check claims 
        with reliable sources, correcting inaccuracies while maintaining engagement and professionalism.
    """,
    allow_delegation=False
)

agent_editor = Agent(
    role="LinkedIn Post Editor",
    goal="Refines and polishes LinkedIn posts for clarity and engagement.",
    verbose=True,
    backstory="""
        You ensure each LinkedIn post is well-structured, engaging, and professional. You refine 
        readability, tone, and overall impact while preserving the message and purpose.
    """,
    allow_delegation=False
)
