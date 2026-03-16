from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# 1. Dokument laden (z.B. "bigdata.md")
loader = TextLoader("bigdata.md")
# 2. Embedding festlegen
embedding = OpenAIEmbeddings()

# 3. Index erstellen (FAISS-Vektordatenbank)
index = VectorstoreIndexCreator(embedding=embedding, text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)).from_loaders([loader])

# 4. Modell: Lokales LLM über Ollama
model = ChatOpenAI(model="gpt-4o-mini")

# 5. Abfrage (Retrieval + Generation)
query = "Welche Vorteile bringt Big Data für Unternehmen?"
answer = index.query(query, llm=model)

print(answer)