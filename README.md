# 🚀 CrewAI LinkedIn Content Generator

Hi! Welcome to my **CrewAI content creation project**. This project experiments with **CrewAI's multi-agent orchestration library** in Python to automate the creation of engaging, fact-checked LinkedIn posts on trending AI and technology topics.  

The logic is simple: each content creation task is divided between specialized agents. CrewAI makes it easy to create agents without much coding, so most of the work focuses on **natural language prompting** rather than heavy software engineering.  

---

## 🤖 Agents
Here’s a description of the agents created:

- **Automated Research:** Fetches trending AI and tech topics from the web.  
- **Topic Selection:** Ensures unique and timely topics.  
- **Content Creation:** Generates LinkedIn-style posts.  
- **Fact-Checking:** Verifies claims for accuracy.  
- **Editing & Refinement:** Polishes content for clarity and engagement.  

Each agent is defined by a **role, goal, backstory, and set of tools**. I used CrewAI's built-in tools to keep it simple. Agents can also delegate tasks to other agents for more complex workflows.  
> Agent definitions can be found in `src/agents`.

---

## 🗂 Tasks and System Orchestration
Tasks are assigned to agents and are defined using natural language prompting. 
The **orchestration system** defines the sequence of operations for the multi-agent workflow. I chose to start with a fairly simple linear one, which is the following:  

**research → topic selection → content creation → fact-checking → refinement**

The orchestration logic is in `src/crew.py`, while task definitions are in `src/tasks.py` and agent implementations in `src/agents.py`.

---

## 📊 Project Preview
The full project execution is available as a Jupyter notebook:  
**`crewai_agent_system_post_generator.ipynb`**  

It demonstrates the workflow from research to final LinkedIn post.

---

## ⚙️ Running the Project

### Setup
1. Install dependencies by running: `pip install -r requirements.txt`.  
2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key  
SERPER_API_KEY=your_serper_api_key  
```

> The Serper API key enables web search functionality. You can get a free API key from their website.

3. Run the generator by executing `src/main.py`.  
> The final post will be saved in `post.md`.

---

## 📝 Notes
- `covered_topics.txt` tracks previously covered topics to avoid duplicates.  
- The system prioritizes **fresh and high-impact discussions**.  
- This project demonstrates **multi-agent orchestration, prompt engineering, and LLM-based automation** in a lightweight Python environment.

---

✨ Enjoy experimenting with CrewAI and exploring AI-powered content generation!
