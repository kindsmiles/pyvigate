from llama_index.core import (Settings,
                              SimpleDirectoryReader,
                              VectorStoreIndex
                              )


class QueryEngine:
    """
    Manages interactions with LLM and embedding services for querying and indexing.
    This class supports different types of LLM services (e.g., Azure OpenAI and Together AI)
    by dynamically initializing the required services based on the specified configuration.
    """
    def __init__(self, api_key, model_name, embedding_name, llm_type='azure', embedding_type='azure',
                 endpoint=None, api_version=None):
        """
        Initializes the QueryEngine with the specified configuration.

        Args:
            api_key (str): The API key for the services.
            model_name (str): The model name for both the LLM and embedding services.
            llm_type (str, optional): The type of LLM ('azure' or 'together'). Defaults to 'azure'.
            embedding_type (str, optional): The type of embedding ('azure' or 'together'). Defaults to 'azure'.
            endpoint (str, optional): The endpoint URL for the service. Required for Azure.
            api_version (str, optional): The API version of the service. Required for Azure.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.embedding_name = embedding_name
        self.llm_type = llm_type
        self.embedding_type = embedding_type
        self.endpoint = endpoint
        self.api_version = api_version

        self.initialize_services()

    def initialize_services(self):
        """Initializes the LLM and embedding models"""

        if self.llm_type == 'azure':
            from llama_index.llms.azure_openai import AzureOpenAI
            self.llm = AzureOpenAI(model=self.model_name, api_key=self.api_key,
                                   azure_endpoint=self.azure_endpoint,
                                   api_version=self.api_version)
        elif self.llm_type == 'together':
            from llama_index.llms.together import TogetherLLM
            self.llm = TogetherLLM(model=self.model_name, api_key=self.api_key)

        if self.embedding_type == 'azure':
            from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
            self.embed_model = AzureOpenAIEmbedding(model=self.embedding_name,
                                                    api_key=self.api_key,
                                                    azure_endpoint=self.azure_endpoint,
                                                    api_version=self.api_version)
        elif self.embedding_type == 'together':
            from llama_index.embeddings.together import TogetherEmbedding
            self.embed_model = TogetherEmbedding(model_name=self.embedding_name,
                                                 api_key=self.api_key)

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

    def create_vector_store_index(self, directory_path):
        """Creates a vector store index from documents in the specified directory."""
        documents = SimpleDirectoryReader(directory_path).load_data()
        return VectorStoreIndex.from_documents(documents)

    def query(self, index, query_text):
        """Queries the provided index with the specified query text and returns the results."""
        query_engine = index.as_query_engine()
        return query_engine.query(query_text)
