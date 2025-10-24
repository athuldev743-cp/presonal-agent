# memory/embeddings.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

embeddings_store = []

def add_to_memory(text):
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding
    embeddings_store.append((text, emb))

def semantic_search(query, top_k=1):
    q_emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding
    # Simple cosine similarity search
    def cosine(a, b):
        return sum(x*y for x, y in zip(a, b)) / ((sum(x*x for x in a)**0.5) * (sum(y*y for y in b)**0.5))
    results = sorted(embeddings_store, key=lambda x: cosine(q_emb, x[1]), reverse=True)
    return [text for text, _ in results[:top_k]]
