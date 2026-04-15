# Project: Multi-Agent AI Orchestrator
# Lead Developer: Sushanth Reddy Kandakatla
# Goal: Automating Startup Workflows & Market Analysis

class StartupAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def perform_task(self, task):
        print(f"[{self.name} - {self.role}]: Starting work on '{task}'...")
        # Future: Integrate OpenAI API here
        return "Task Analysis Complete."

if __name__ == "__main__":
    # Initializing our first Startup Agent
    ceo_agent = StartupAgent("Bull_One", "Market Analyst")
    ceo_agent.perform_task("Analyzing stock trends for AI-driven startups")
