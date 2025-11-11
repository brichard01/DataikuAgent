import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel
import tools

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_key=api_key,
)

tools = [
    #tools.ExtractCompaniesTool(),
    tools.CheckClientStatusTool(),
]

news = """
Renault and Stellantis are collaborating on new EV battery factories in France.
This could reshape the European automotive market.
"""

prompt = f"""
You are a financial news monitoring agent for the bank.
Analyze the following news:
\"\"\"{news}\"\"\"

Steps:
1. Extract any companies mentioned using the Extract Companies tool.
2. For each company, check if it is an existing client using Check Client Status.
3. Produce a short summary for the client manager that should be alerted.
"""

prompt = f"""
You are a financial news monitoring agent for the bank.
Analyze the following news:
\"\"\"{news}\"\"\"

Steps:
1. Identify every company mentioned in the text.
2. For each company, check if it is an existing client using Check Client Status.
3. If it is an existing client only, write a brief summary of the news and how it will impact the client.
"""

agent = CodeAgent(tools=tools, model=model)
response = 'ok'
response = agent.run(prompt)

print("Final output:")
print(response)

