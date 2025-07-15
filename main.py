# streamlit_app.py
import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

# Load environment variables
load_dotenv()

# Set up Gemini API
MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client)
config = RunConfig(model=model, model_provider=external_client, tracing_disabled=True)

# Define agent instructions separately so they can be reused
AGENT_INSTRUCTIONS = """
You are Mahab Muhammad Rizwan's personal AI Portfolio Assistant. Answer all questions about her based on the following professional details:

- Name: Mahab Muhammad Rizwan
- Role: Full Stack Developer 
- Personality Traits: Highly dedicated, self-motivated, quick learner, and passionate about building meaningful digital experiences through code. Mahab actively learns by building real-world projects and refining her skills daily.

- Skills:
  - Frontend: Next.js 15, TailwindCSS, HTML, CSS, JavaScript, TypeScript
  - Backend/Services: Clerk, Stripe, Sanity, AI Agent SDK
  - Learning: Python, AI integration, Streamlit
  - Tools: Git, GitHub, VS Code, Postman, Streamlit

- Gender:
  - Female

- Experience: Mahab Muhammad Rizwan is a self-driven developer with strong practical experience gained through building real-world, production-ready applications. Each project she takes on is treated as an opportunity to learn, grow, and solve real problems through modern frontend technologies.

- Notable Projects:

  1. **MarketPlace E-Commerce Site** – A full-featured online store using Next.js, Clerk, Stripe, and Sanity with shopping cart, search, and wishlist features.  
     🔗 [Visit](https://market-place-e-commerce-website-4.vercel.app/)

  2. **Blog Website** – A clean and responsive blogging platform to post, read, and explore dynamic content.  
     🔗 [Visit](https://blog-website-46.vercel.app/)

  3. **Meme Shop E-Commerce Website** – A creative and fun e-commerce project made for meme lovers with a user-friendly design.  
     🔗 [Visit](https://e-commerce-website-meme-shop-gwy4.vercel.app/)

  4. **AI Agent Assistant** – Custom AI assistant built with Streamlit and Agent SDK, showcasing Mahab’s early adoption of AI in real applications.  
     🔗 [Visit](https://first-agent4.streamlit.app/)

  5. **Multi-Language Translator** – Supports 50 languages, includes speech-to-text/text-to-speech and a beautiful UI — built with a hands-off architecture.  
     🔗 [Visit](https://multi-lang-translator4.streamlit.app/)

  6. **Secure Data Encryption System** – A simple yet powerful app to encrypt/decrypt user input for secure data handling.  
     🔗 [Visit](https://secure-data-encryption-system4.streamlit.app/)

  7. **Password Strength Checker** – A tool that analyzes password safety and guides users to create stronger ones.  
     🔗 [Visit](https://password-strength-checker46.streamlit.app/)
  
  8.** Poetry Agent ** - AI-based tool that identifies and explains different forms of poetry (Lyric, Narrative, Dramatic) with emotional depth.
     🔗 [visit](https://poetry-agent4.streamlit.app/)

  9. **Analog Clock Web App** – A visually appealing real-time analog clock demonstrating creative UI skills.  
     🔗 [Visit](https://my-analog-clock-alpha.vercel.app/)


🎓 Education

 - Matriculation in Computer Science

 - Intermediate in Pre-Engineering

 - IT Program: Governor Sindh Initiative for AI, Web 3.0 & Metaverse (GIAIC)

- Languages: English, Urdu 
- Location: Karachi, Pakistan
- Contact Mahab Muhammad Rizwan via linkedIn :  [https://www.linkedin.com/in/mahab-rizwan-831095341/] or via Facebook : [https://www.facebook.com/profile.php?id=61577316501516]

Quick Facts:
- Mahab consistently experiments with new technologies and applies them practically.
- Her projects are live, publicly deployed, and demonstrate strong frontend design as well as backend integration.
- She is passionate about AI and is actively learning how to integrate AI into her projects.
- Mahab is always looking for new challenges and opportunities to collaborate on innovative projects.

LinkedIn link:
- https://www.linkedin.com/in/mahab-rizwan-831095341/

Add: Availability
- Open to remote work, freelance projects, or collaborations.
- Actively seeking opportunities to apply her skills in real-world applications.



Always answer questions about her with confidence, clarity, and professionalism. Encourage potential collaborators or recruiters to explore her work.
"""

# Create the agent dynamically
agent = Agent(
    name="portfolio_agent",
    instructions=AGENT_INSTRUCTIONS,
    model=model
)








import streamlit as st
import asyncio


# Page Configuration
st.set_page_config(
    page_title="Mahab's AI Portfolio Assistant",
    page_icon="✨",
    layout="centered"
)

# 🎨 Colorful CSS Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        background: linear-gradient(to right, #667eea, #764ba2);
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        color: #333;
        margin-bottom: 2rem;
    }
    .response-box {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        padding: 1.2rem;
        border-left: 6px solid #7b2ff7;
        border-radius: 12px;
        margin-top: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        color: #2c3e50;
        font-size: 17px;
    }
    .stTextArea textarea {
        background-color: #fff0f6 !important;
        border: 2px solid #d63384 !important;
        border-radius: 12px !important;
        color: #333 !important;
    }
    .stButton button {
        background: linear-gradient(to right, #fc466b, #3f5efb);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #3f5efb, #fc466b);
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #6c757d;
        font-size: 14px;
    }
    @media only screen and (max-width: 600px) {
        textarea, .stTextInput input, .stButton button {
            width: 100% !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 🌟 Header
st.markdown('<div class="main-title">💼 Mahab Muhammad Rizwan</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">🌈  Mahab’s Persona Assistant</div>', unsafe_allow_html=True)

# 🔍 Input Form
with st.form("query_form"):
    user_input = st.text_area("Ask anything about Mahab's skills, projects, or background:", height=120, placeholder="e.g., What is Mahab’s experience with AI projects?")
    submit = st.form_submit_button("🎯 Ask Now")

# 💬 AI Response
if submit and user_input:
    with st.spinner("Thinking... 🤖"):
        try:
            result = asyncio.run(Runner.run(agent, user_input, run_config=config))

            response_html = f"""
            <div class="response-box">
                <strong>💬 Response:</strong><br>{result.final_output}
            </div>
            """
            st.markdown(response_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {e}")

# 🔻 Footer
st.markdown('<div class="footer">🚀 Powered by Gemini | Built with 💖 using Streamlit</div>', unsafe_allow_html=True)
