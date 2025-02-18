from crewai import Crew
from agents import agent_researcher, agent_topic_selector, agent_writer, agent_fact_checker, agent_editor
from tasks import task_research, task_select_topic, task_write_post, task_fact_check_post, task_edit_post

community_management_crew = Crew(
    agents=[agent_researcher, agent_topic_selector, agent_writer, agent_fact_checker, agent_editor],
    tasks=[task_research, task_select_topic, task_write_post, task_fact_check_post, task_edit_post],
    verbose=True
)

def run_crew():
    return community_management_crew.kickoff()
