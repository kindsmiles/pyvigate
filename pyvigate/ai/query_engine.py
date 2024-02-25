from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex


class QueryEngine:
    """
    Manages interactions with different LLM and embedding services for
    querying and indexing, supporting dynamic service initialization.
    """

    def __init__(self, api_key, model_name, embedding_name, llm_type='azure',
                 embedding_type='azure', endpoint=None, api_version=None):
        """
        Initializes QueryEngine with specific service configurations.

        Args:
            api_key (str): API key for the LLM and embedding services.
            model_name (str): Model name for the LLM service.
            embedding_name (str): Model name for the embedding service.
            llm_type (str): Type of LLM service ('azure' or 'together').
            embedding_type (str): Type of embedding service ('azure' or 'together').
            endpoint (str, optional): Endpoint URL for the service, for Azure.
            api_version (str, optional): API version for the service, for Azure.
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
        """
        Initializes the specified LLM and embedding services based on config.
        """
        if self.llm_type == 'azure':
            from llama_index.llms.azure_openai import AzureOpenAI
            self.llm = AzureOpenAI(api_key=self.api_key,
                                   azure_endpoint=self.endpoint,
                                   model=self.model_name,
                                   api_version=self.api_version)
        elif self.llm_type == 'together':
            from llama_index.llms.together import TogetherLLM
            self.llm = TogetherLLM(api_key=self.api_key,
                                   model=self.model_name)

        if self.embedding_type == 'azure':
            from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
            self.embed_model = AzureOpenAIEmbedding(api_key=self.api_key,
                                                    azure_endpoint=self.endpoint,
                                                    model=self.embedding_name,
                                                    api_version=self.api_version)
        elif self.embedding_type == 'together':
            from llama_index.embeddings.together import TogetherEmbedding
            self.embed_model = TogetherEmbedding(api_key=self.api_key,
                                                 model=self.embedding_name)

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

    def create_vector_store_index(self, directory_path):
        """
        Creates a vector index from documents in a specified directory.
        """
        documents = SimpleDirectoryReader(directory_path).load_data()
        return VectorStoreIndex.from_documents(documents)

    def query(self, index, query_text):
        """
        Queries an index with text and returns the results.
        """
        query_engine = index.as_query_engine()
        return query_engine.query(query_text)
