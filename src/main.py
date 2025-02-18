from crew import run_crew
from IPython.display import Markdown, display

result = run_crew()
display(Markdown("./post.md"))
