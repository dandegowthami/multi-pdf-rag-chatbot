import uuid
import chromadb


class VectorService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vectorstore"
        )

        self.collection = self.client.get_or_create_collection(
            name="pdf_documents"
        )

    def store_embeddings(
        self,
        chunks,
        embeddings,
        pdf_name
    ):

        ids = []
        metadatas = []

        for index, chunk in enumerate(chunks):

            unique_id = (
                f"{pdf_name}_{index}_{uuid.uuid4()}"
            )

            ids.append(unique_id)

            metadatas.append(
                {
                    "pdf_name": pdf_name,
                    "chunk_id": index
                }
            )

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

        return len(chunks)

    def get_total_chunks(self):

        return self.collection.count()

    def search_documents(
    self,
    query_embedding,
    top_k=5
    ):

        results = self.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k
        )

        return results

    def get_all_documents(self):

        results = self.collection.get()

        pdf_files = set()

        for metadata in results["metadatas"]:

            pdf_files.add(
                metadata["pdf_name"]
            )

        return list(pdf_files)

    def clear_database(self):

        all_data = self.collection.get()

        if all_data["ids"]:

            self.collection.delete(
                ids=all_data["ids"]
            )

        return True 
    def delete_document(
    self,
    pdf_name
):

        results = self.collection.get(
            where={
                "pdf_name": pdf_name
            }
        )

        ids_to_delete = results["ids"]

        if ids_to_delete:

            self.collection.delete(
                ids=ids_to_delete
            )

        return len(ids_to_delete)