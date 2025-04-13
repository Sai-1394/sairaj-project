import google.generativeai as genai
import gradio as gr

# Set your Gemini API key
genai.configure(api_key="AIzaSyDdJ34Uq0loWzdrsa_NNyAQqYpcTHShQro")

# Load Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Function to ask Gemini
def ask_gemini(question, subject):
    prompt = f"""
    You are an expert tutor helping a college student prepare for exams. 
    Explain this question in a simple and beginner-friendly way.

    Subject: {subject}
    Question: {question}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=ask_gemini,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your exam question here..."),
        gr.Textbox(placeholder="Enter subject (e.g., Physics, Math, DBMS)...")
    ],
    outputs="text",
    title="📘 Exam Prep Chatbot (Gemini)",
    description="Get easy explanations for your toughest subjects. Powered by Google Gemini Pro."
)

iface.launch()
