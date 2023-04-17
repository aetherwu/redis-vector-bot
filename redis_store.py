# Check one of the products
# product_metadata[0]
import os
 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore

from create_meta import createMeta
from redisearch import Client, IndexDefinition
import redis

# set your openAI api key as an environment variable
os.environ['OPENAI_API_KEY'] = ""

# Function to check if the index exists
def checkIndex(client, index_name):
    try:
        client.info()
        return True
    except Exception as e:
        if "Unknown index name" in str(e):
            return False
        else:
            raise

def getRedisStore(index_name=None, product_metadata=None):
    
    # Connect to Redis server
    redisURL = 'redis://localhost:6379'
    embedding = OpenAIEmbeddings()
    index_exists = False

    if index_name:
        print(f"Looking for index '{index_name}'.")
        redis_client = redis.Redis.from_url(redisURL)
        search_client = Client(index_name, conn=redis_client)
        if checkIndex(search_client, index_name):
            index_exists = True
            print(f"The index '{index_name}' found.")
        else:
            print(f"Index '{index_name}' not found")
    else:
        print(f"Index name '{index_name}' does not provided")
        return None

    # Check if the index exists
    if index_exists:
        # Create RedisVectorStore object from existing index
        vectorstore = RedisVectorStore.from_existing_index(embedding, redis_url=redisURL, index_name=index_name)
    else:

        if product_metadata is None:
            product_metadata = createMeta()
        
        texts = [
            v['item_name'] for k, v in product_metadata.items()
        ]
        
        # product metadata that we'll store along our vectors
        metadatas = list(product_metadata.values())
        
        # create and load redis with documents
        vectorstore = RedisVectorStore.from_texts(
            texts=texts,
            metadatas=metadatas,
            embedding=embedding,
            index_name=index_name,
            redis_url=redisURL
        )

    return vectorstore