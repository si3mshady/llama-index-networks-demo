import asyncio
from llama_index.networks.contributor import ContributorClient
from llama_index.networks.query_engine import NetworkQueryEngine
from llama_index.llms.openai import OpenAI

# Use ContributorClient to connect to a ContributorService
client1 = ContributorClient.from_config_file(env_file=".env.contributer1")
client2 = ContributorClient.from_config_file(env_file=".env.contributer2")

contributors = [client1, client2]

# NetworkQueryEngine
llm = OpenAI()
network_query_engine = NetworkQueryEngine.from_args(
    contributors=contributors, llm=llm
)
# query = "What is Sora? Explain in simple terms"
query = "What is Diffuser Transformer? Explain in simple terms"


async_res =  asyncio.run( network_query_engine.aquery(query))
print(async_res)
