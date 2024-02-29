import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.networks.contributor import (
    ContributorServiceSettings,
    ContributorService,
)

# Set the port using an environment variable or default to 8000
port = int(os.getenv("PORT", 8000))

# Load data from the "data" directory
documents = SimpleDirectoryReader("data2").load_data()

# Create a VectorStoreIndex from the loaded documents
index = VectorStoreIndex.from_documents(documents)


# Create a query engine from the index
query_engine = index.as_query_engine()

# Initialize ContributorServiceSettings
settings = ContributorServiceSettings()



# Initialize ContributorService with configuration and query engine
service = ContributorService(config=settings, query_engine=query_engine)
app = service.app

if __name__ == "__main__":
    import uvicorn

    # Run the app using uvicorn with the specified port
    uvicorn.run(app, host="0.0.0.0", port=port)