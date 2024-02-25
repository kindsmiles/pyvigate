# Module `query_engine`

## Class `QueryEngine`

    Manages interactions with different LLM and embedding services for
    querying and indexing, supporting dynamic service initialization.

### Attributes:


### Methods:

- **__init__**`(self, api_key, model_name, embedding_name, llm_type='azure', embedding_type='azure', endpoint=None, api_version=None)`

    Initializes QueryEngine with specific service configurations.
    
    Args:
        api_key (str): API key for the LLM and embedding services.
        model_name (str): Model name for the LLM service.
        embedding_name (str): Model name for the embedding service.
        llm_type (str): Type of LLM service ('azure' or 'together').
        embedding_type (str): Type of embedding service ('azure' or 'together').
        endpoint (str, optional): Endpoint URL for the service, for Azure.
        api_version (str, optional): API version for the service, for Azure.

- **create_vector_store_index**`(self, directory_path)`

    Creates a vector index from documents in a specified directory.

- **initialize_services**`(self)`

    Initializes the specified LLM and embedding services based on config.

- **query**`(self, index, query_text)`

    Queries an index with text and returns the results.

