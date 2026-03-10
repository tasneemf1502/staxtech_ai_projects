import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
with open("dataset/faq_data.json") as file:
    data = json.load(file)

patterns = []
responses = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(random.choice(intent["responses"]))

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(patterns)

def get_response(user_input):

    user_vec = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vec, X)

    score = similarity.max()
    index = similarity.argmax()

    if score < 0.25:
        return "I'm not sure about that. Please ask about the internship."

    return responses[index]