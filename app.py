import gradio as gr
from groq import Groq
import os

# Get your key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# Analysis function
def validate_idea(idea):
    if not idea.strip():
        return "❌ Please enter a startup idea."

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You're a startup analyst who evaluates business ideas."},
            {"role": "user", "content": f"Analyze the following startup idea:\n\n{idea}\n\nGive a brief SWOT analysis, potential audience, tech feasibility, and market fit."}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# Gradio Interface
gr.Interface(
    fn=validate_idea,
    inputs=gr.Textbox(label="Your Startup Idea", lines=6, placeholder="Describe your idea..."),
    outputs=gr.Markdown(label="AI Validation Report"),
    title="🚀 Startup Idea Validator",
    description="Validate your startup idea using Groq's LLM."
).launch()
