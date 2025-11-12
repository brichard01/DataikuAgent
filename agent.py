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
    Renault announced today a strategic partnership with Google Cloud to accelerate the deployment of artificial intelligence in its manufacturing operations.
    The collaboration aims to optimize production lines through predictive maintenance and energy efficiency solutions.
    This initiative is part of Renault’s broader strategy to digitize its industrial ecosystem and reduce operational costs by 20% over the next three years.
    Analysts suggest this move could strengthen Renault’s competitive position in the European automotive market, especially amid increasing competition from Stellantis and Volkswagen.
    """

    response = run_agent(news)

    print("Final output:")
    print(response)



