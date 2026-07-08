from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, chunks):

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True
        )

        return embeddings

    def generate_query_embedding(
        self,
        question
    ):

        query_embedding = self.model.encode(
            question,
            convert_to_numpy=True
        )

        return query_embedding