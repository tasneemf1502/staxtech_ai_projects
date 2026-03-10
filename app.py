import streamlit as st
import json
import random

# -------- LOAD DATASET --------

with open("dataset/faq_data.json") as file:
    data = json.load(file)


# -------- GREETING DETECTION --------

def check_greeting(user_input):

    greetings = ["hi", "hello", "hey", "how are you", "good morning", "good evening"]

    user_input = user_input.lower()

    for word in greetings:
        if word in user_input:
            return """Hello 👋  
I am the **StaxTech AI Internship Assistant**.

I can help you with:

• Internship details  
• Project suggestions  
• Domain recommendations  
• Certificate information  

Try asking something like:

• What is the StaxTech internship?  
• Suggest beginner projects  
• I like coding and mathematics  
• How to contact StaxTech
"""
    return None


# -------- DOMAIN RECOMMENDATION --------

def recommend_domain(user_input):

    user_input = user_input.lower()

    if "ai" in user_input or "artificial intelligence" in user_input:
        return "🤖 Recommended Domain: Artificial Intelligence"

    elif "machine learning" in user_input or "math" in user_input or "statistics" in user_input:
        return "📊 Recommended Domain: Machine Learning"

    elif "frontend" in user_input or "front end" in user_input or "ui" in user_input or "ux" in user_input or "design" in user_input:
        return "🎨 Recommended Domain: Frontend Development (UI/UX)"

    elif "backend" in user_input or "back end" in user_input or "api" in user_input or "server" in user_input:
        return "⚙ Recommended Domain: Backend Development"

    elif "full stack" in user_input:
        return "🌐 Recommended Domain: Full Stack Development"

    elif "cloud" in user_input or "aws" in user_input or "deployment" in user_input:
        return "☁ Recommended Domain: Cloud Computing"

    elif "coding" in user_input or "programming" in user_input:
        return "💻 Recommended Domain: Software Development"

    elif "data" in user_input:
        return "📊 Recommended Domain: Data Science / Machine Learning"

    return None


# -------- PROJECT RECOMMENDATION --------

def recommend_project(user_input):

    user_input = user_input.lower()

    if "beginner" in user_input:
        return "Beginner Projects: Calculator, To Do List, Quiz Game, Password Generator."

    elif "intermediate" in user_input:
        return "Intermediate Projects: Weather App, Currency Converter, Rock Paper Scissors."

    elif "advanced" in user_input:
        return "Advanced Projects: Blog Website, E Commerce Website, Student Management System."

    return None


# -------- FAQ BOT --------

def get_bot_response(user_input):

    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return """Sorry, I didn't understand that.

You can ask things like:

• What is the StaxTech internship?
• Suggest beginner projects
• What is portfolio project?
• How to contact StaxTech
"""


# -------- STREAMLIT UI --------

st.title("StaxTech AI Internship Assistant 🤖")

st.write(
"This AI assistant helps students explore the StaxTech internship platform, discover projects and choose the right learning domain."
)


# -------- SIDEBAR SUPPORT --------

st.sidebar.title("Support")

st.sidebar.write("📧 Email: Staxtechinfo@gmail.com")
st.sidebar.write("👤 Founder: Mr Pawan Kushwaha")
st.sidebar.write("🔗 LinkedIn: StaxTech")


# -------- QUICK SUGGESTIONS --------

st.subheader("Quick Questions")

suggestions = [
"What is StaxTech internship?",
"Suggest beginner projects",
"I like coding and mathematics",
"How to verify certificate?",
"How to contact StaxTech?"
]


for s in suggestions:

    if st.button(s):

        user_input = s

        greet = check_greeting(user_input)

        if greet:
            st.success(greet)

        else:

            domain = recommend_domain(user_input)
            project = recommend_project(user_input)

            if domain:
                st.success(domain)

            if project:
                st.success(project)

            if not domain and not project:
                response = get_bot_response(user_input)
                st.info(response)


# -------- CHAT INPUT --------

st.subheader("Ask the Assistant")

user_input = st.text_input("Type your question")

if user_input:

    greet = check_greeting(user_input)

    if greet:
        st.success(greet)

    else:

        domain = recommend_domain(user_input)
        project = recommend_project(user_input)

        if domain:
            st.success(domain)

        if project:
            st.success(project)

        if not domain and not project:
            response = get_bot_response(user_input)
            st.info(response)