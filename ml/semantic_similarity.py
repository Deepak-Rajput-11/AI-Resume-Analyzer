from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(resume_text, jd_text):

    embeddings = model.encode([resume_text, jd_text])

    similarity = cosine_similarity(embeddings[0:1], embeddings[1:2])

    return round(float(similarity[0][0]) * 100, 2)
