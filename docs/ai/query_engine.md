# Module `query_engine`

## Class `QueryEngine`

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

### Attributes:


### Methods:

- **__init__**`(self, api_key, api_version, azure_endpoint, llm_deployment_name, embedding_deployment_name)`

No description provided.

- **create_vector_store_index**`(self, directory_path)`

    Creates a vector store index from the documents
    within the specified directory path.
    
    Parameters:
        directory_path (str): The path to the directory containing
        the documents to be indexed.
    
    Returns:
        VectorStoreIndex: An instance of VectorStoreIndex
        containing the indexed documents.

- **query**`(self, index, query_text)`

    Queries the provided index with the specified query text
    and returns the results.
    
    Parameters:
        index (VectorStoreIndex): The index to query against.
        query_text (str): The text to query the index with.
    
    Returns:
        Any: The results of the query against the index.

