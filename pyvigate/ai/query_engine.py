
from llama_index import (
    ServiceContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
    set_global_service_context,
)
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.llms import AzureOpenAI


class QueryEngine:
    """
    A class that initializes and manages interactions with
    a Large Language Model (LLM) and embedding services
    for querying and indexing documents using the Azure OpenAI service.

    Attributes:
        api_key (str): API key for Azure OpenAI services.
        api_version (str): The API version of the Azure OpenAI service.
        azure_endpoint (str): The endpoint URL for the Azure OpenAI service.
        llm_deployment_name (str): The deployment name for the LLM service.
        embedding_deployment_name (str): The deployment name for the embedding.
        llm (AzureOpenAI): An instance of the AzureOpenAI class for LLM.
        embed_model (AzureOpenAIEmbedding): AzureOpenAIEmbedding instance
        service_context (ServiceContext): Config for LLM and Embedding models.

    Methods:
        create_vector_store_index(directory_path): Creates a vector store index
        from documents in a specified directory.
        query(index, query_text): Queries an index with a given text
        and returns the query results.
    """

    def __init__(
        self,
        api_key,
        api_version,
        azure_endpoint,
        llm_deployment_name,
        embedding_deployment_name,
    ):
        self.api_key = api_key
        self.api_version = api_version
        self.azure_endpoint = azure_endpoint
        self.llm_deployment_name = llm_deployment_name
        self.embedding_deployment_name = embedding_deployment_name

        self.llm = AzureOpenAI(
            model="gpt-35-turbo",
            deployment_name=self.llm_deployment_name,
            api_key=self.api_key,
            azure_endpoint=self.azure_endpoint,
            api_version=self.api_version,
        )

        self.embed_model = AzureOpenAIEmbedding(
            model="text-embedding-ada-002",
            deployment_name=self.embedding_deployment_name,
            api_key=self.api_key,
            azure_endpoint=self.azure_endpoint,
            api_version=self.api_version,
        )

        self.service_context = ServiceContext.from_defaults(
            llm=self.llm,
            embed_model=self.embed_model,
        )

        set_global_service_context(self.service_context)

    def create_vector_store_index(self, directory_path):
        """
    Creates a vector store index from the documents
    within the specified directory path.

    Parameters:
        directory_path (str): The path to the directory containing
        the documents to be indexed.

    Returns:
        VectorStoreIndex: An instance of VectorStoreIndex
        containing the indexed documents.
    """
        documents = SimpleDirectoryReader(directory_path).load_data()
        return VectorStoreIndex.from_documents(
            documents, service_context=self.service_context
        )

    def query(self, index, query_text):
        """
    Queries the provided index with the specified query text
    and returns the results.

    Parameters:
        index (VectorStoreIndex): The index to query against.
        query_text (str): The text to query the index with.

    Returns:
        Any: The results of the query against the index.
    """
        query_engine = index.as_query_engine()
        return query_engine.query(query_text)
