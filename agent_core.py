from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama

# Using the power of your Lenovo LOQ locally
local_llm = Ollama(model="llama3")

# Agent 1: The ML Architect
# Focuses on the technical stack and model selection
architect = Agent(
  role='Principal ML Architect',
  goal='Design the most efficient AI architecture for a new SaaS product',
  backstory='Expert in LLMs, RAG pipelines, and scalable GPU infrastructure.',
  llm=local_llm,
  verbose=True
)

# Agent 2: The Tech Lead
# Converts the architecture into a development roadmap
tech_lead = Agent(
  role='Senior Tech Lead',
  goal='Create a 12-week development sprint plan based on the ML architecture',
  backstory='Specialist in Agile methodology and full-stack AI integration.',
  llm=local_llm,
  verbose=True
)

# Define technical tasks
task1 = Task(
    description="Design a scalable RAG (Retrieval-Augmented Generation) system for a coding assistant.",
    agent=architect,
    expected_output="A technical specification document detailing vector database and LLM choice."
)

task2 = Task(
    description="Develop a 12-week roadmap for building the MVP based on the architect's design.",
    agent=tech_lead,
    expected_output="A week-by-week breakdown of engineering tasks."
)

# Assemble the Crew
ai_startup_crew = Crew(
  agents=[architect, tech_lead],
  tasks=[task1, task2],
  verbose=2
)

print("### ORCHESTRATION STARTING ###")
result = ai_startup_crew.start()
print("\n### FINAL STARTUP ROADMAP ###")
print(result)
