from crewai import Agent, Task, Crew
from langchain.llms import Ollama

# Initialize Ollama
ollama_llm = Ollama(model="llama2")

# Define Agents
researcher = Agent(
    role="Tech Researcher",
    goal="Find cutting-edge AI developments",
    backstory="A curious AI researcher who loves discovering breakthroughs.",
    llm=ollama_llm,
    verbose=True
)

writer = Agent(
    role="Technical Writer",
    goal="Write engaging articles about AI",
    backstory="A writer who simplifies complex tech topics for readers.",
    llm=ollama_llm,
    verbose=True
)

# Define Tasks
research_task = Task(
    description="Find the latest advancements in AI in 2024.",
    agent=researcher
)

write_task = Task(
    description="Write a short blog post about AI trends in 2024.",
    agent=writer
)

# Assemble Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=2
)

# Execute!
result = crew.kickoff()
print("Result:")
print(result)
