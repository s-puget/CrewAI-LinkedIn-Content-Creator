from crewai import Task
from datetime import date
from agents import agent_researcher, agent_topic_selector, agent_writer, agent_fact_checker, agent_editor

current_date = date.today()

task_research = Task(
    description=f"""
        Search the web for trending AI and technology topics for today ({current_date}). 
        Provide a ranked list of 5 topics, marking one as 'Very Important' if applicable.
    """,
    expected_output="A ranked list of 5 trending topics, with one marked as 'Very Important' if applicable.",
    agent=agent_researcher
)

task_select_topic = Task(
    description="""
        Analyze the ranked topics and compare them with 'covered_topics.txt'. Select a new, relevant 
        topic, prioritizing the 'Very Important' topic if it has not been covered recently.
    """,
    expected_output="One unique, relevant topic that has not been covered recently.",
    agent=agent_topic_selector,
    context=[task_research]
)

task_write_post = Task(
    description=f"""
        Write a concise LinkedIn-style post about the selected topic. Ensure it is informative, 
        engaging, and relevant, with a tone suited for LinkedIn. Today is {current_date}.
    """,
    expected_output="A well-written LinkedIn post of 150-200 words.",
    agent=agent_writer,
    context=[task_select_topic]
)

task_fact_check_post = Task(
    description=f"""
        Review the LinkedIn post for factual accuracy and credibility. Verify all claims using 
        reliable sources and provide actionable corrections if necessary.
    """,
    expected_output="A LinkedIn post with factual issues corrected, if applicable.",
    agent=agent_fact_checker,
    context=[task_write_post]
)

task_edit_post = Task(
    description="""
        Edit the LinkedIn post for clarity, engagement, and professionalism. Apply fact-checking 
        feedback and ensure the post is polished and ready for publication.
    """,
    expected_output="A refined LinkedIn post, free from grammatical and factual errors.",
    agent=agent_editor,
    context=[task_write_post, task_fact_check_post],
    output_file="post.md"
)
