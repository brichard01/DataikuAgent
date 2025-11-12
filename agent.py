import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel
import tools
from prompts import output_format, prompt

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_key=api_key,
)

tools = [
    tools.CheckClientStatusTool(),
    tools.CheckClientRelationsTool()
]

agent = CodeAgent(tools=tools, model=model)

def run_agent(news):
    input = prompt.format(
        news=news,
        output_format=output_format,
    )
    return agent.run(input)

if __name__=='__main__':
    news = """
    Renault announced a major expansion of its partnership with Google Cloud to accelerate the integration of artificial intelligence across its manufacturing and supply chain operations.
    By leveraging Google’s advanced data analytics and machine learning platforms, Renault aims to significantly improve production efficiency, reduce energy consumption, and speed up new vehicle development cycles.
    Industry experts view this collaboration as a key milestone in Renault’s digital transformation, giving the automaker a substantial competitive edge in the European market.
    Meanwhile, analysts warn that competitors such as Stellantis could struggle to keep pace, as their digital capabilities and industrial data strategies remain several years behind Renault’s new AI-driven model."""


    response = run_agent(news)

    print("Final output:")
    print(response)



