# CrewAI LinkedIn Content Generator

This project automates the generation of engaging and relevant LinkedIn posts on trending AI and technology topics using **CrewAI**.

## Features
- **Automated Research:** Fetches trending AI and tech topics from the web.
- **Topic Selection:** Ensures unique and timely topics.
- **Content Creation:** Generates LinkedIn-style posts.
- **Fact-Checking:** Verifies claims for accuracy.
- **Editing & Refinement:** Polishes content for clarity and engagement.

## Project Structure

```bash
CrewAI-LinkedIn-Content-Creator/
│── src/
│ │── main.py
│ │── agents.py
│ │── tasks.py
│ │── crew.py
│── covered_topics.txt
│── crewai_agent_system_post_generator.ipynb
│── requirements.txt
│── README.md
```


## Setup
1. Install dependencies using `requirements.txt`.
2. Set API keys in a `.env` file:  
`OPENAI_API_KEY=your_openai_api_key`   
`SERPER_API_KEY=your_serper_api_key`
3. Run `main.py` to generate a LinkedIn post.

## How It Works
1. **Research:** Fetches trending AI topics.
2. **Selection:** Picks the most relevant and unique topic.
3. **Writing:** Creates a LinkedIn-style post.
4. **Fact-Checking:** Verifies claims for accuracy.
5. **Editing:** Refines the final version.
6. **Output:** Saves the post in `post.md`.

## Notes
- `covered_topics.txt` tracks previously covered topics.
- The system prioritizes fresh and high-impact discussions.




