from app.services.pdf_service import extract_text
from app.services.chunk_service import create_chunks
from app.services.embedding_service import EmbeddingService

pdf_path = "data/pdfs/Final_Year_Placement_Roadmap_Gowthami.pdf"

text = extract_text(pdf_path)

chunks = create_chunks(text)

embeddings = EmbeddingService.generate_embeddings(chunks)

print(f"Total Chunks: {len(chunks)}")

print(f"Embedding Shape: {embeddings.shape}")

print("\nFirst Embedding:\n")

print(embeddings[0])