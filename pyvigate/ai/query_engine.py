
from llama_index import (
    ServiceContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
    set_global_service_context,
)
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.llms import AzureOpenAI


class QueryEngine:
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
        documents = SimpleDirectoryReader(directory_path).load_data()
        return VectorStoreIndex.from_documents(
            documents, service_context=self.service_context
        )

    def query(self, index, query_text):
        query_engine = index.as_query_engine()
        return query_engine.query(query_text)
