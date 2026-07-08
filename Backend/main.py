from fastapi import FastAPI, UploadFile, File
from app.services.pdf_service import extract_text
from app.services.chunk_service import create_chunks
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.models.question import QuestionRequest
from app.services.llm_service import LLMService
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()
embedding_service = EmbeddingService()
vector_service = VectorService()
llm_service = LLMService()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "Multi PDF RAG Chatbot Backend Running"
    }

@app.get("/stats")
def get_stats():

    return {
        "total_chunks":
        vector_service.get_total_chunks()
    }
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # Save PDF
    file_path = f"data/pdfs/{file.filename}"

    content = await file.read()

    with open(file_path, "wb") as pdf_file:
        pdf_file.write(content)

    # Extract Text
    text = extract_text(file_path)

    # Create Chunks
    chunks = create_chunks(text)

    # Generate Embeddings
    embeddings = embedding_service.generate_embeddings(
        chunks
    )
    stored_chunks = vector_service.store_embeddings(
    chunks,
    embeddings,
    file.filename
)
    return {
        "filename": file.filename,
        "characters": len(text),
        "total_chunks": len(chunks),
        "stored_chunks":stored_chunks,
        "embedding_dimension": len(embeddings[0]),
        "status": "PDF Processed Successfully"
    }
@app.get("/documents")
def get_documents():

    documents = (
        vector_service
        .get_all_documents()
    )

    return {
        "documents": documents
    }
@app.delete("/clear")
def clear_database():

    vector_service.clear_database()

    pdf_folder = "data/pdfs"

    for file_name in os.listdir(
        pdf_folder
    ):

        file_path = os.path.join(
            pdf_folder,
            file_name
        )

        if os.path.isfile(
            file_path
        ):
            os.remove(
                file_path
            )

    return {
        "message":
        "Database and PDFs cleared successfully"
    }
    
@app.delete("/document/{pdf_name}")
def delete_document(pdf_name: str):

    deleted_chunks = (
        vector_service.delete_document(
            pdf_name
        )
    )

    pdf_path = os.path.join(
        "data",
        "pdfs",
        pdf_name
    )

    if os.path.exists(pdf_path):

        os.remove(pdf_path)

    return {

        "message":
        "Document deleted successfully",

        "document":
        pdf_name,

        "deleted_chunks":
        deleted_chunks
    }
@app.post("/ask")
def ask_question(request: QuestionRequest):

    query_embedding = (
        embedding_service
        .generate_query_embedding(
            request.question
        )
    )

    results = (
        vector_service
        .search_documents(
            query_embedding
        )
    )

    retrieved_chunks = (
        results["documents"][0]
    )
    sources = []

    for metadata in results["metadatas"][0]:

        pdf_name= metadata["pdf_name"]

        if pdf_name not in sources:
            sources.append(pdf_name)
        
    context = "\n\n".join(
        retrieved_chunks
    )

    answer = (
        llm_service.generate_answer(
            request.question,
            context
        )
    )

    return {
    "question": request.question,
    "answer": answer,
    "sources": sources
    }
    return results