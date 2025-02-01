import streamlit as st
import requests


st.set_page_config(page_title="AI Video Q&A", page_icon="🤖", layout="centered")


# Streamlit interface
st.title("AI Q&A with Video Context")

st.markdown("""
Provide a YouTube video link and your question. The AI will process the video transcript and answer your question based on the content.
""")

# Inputs
video_url = st.text_input("🎥 YouTube Video Link", placeholder="Enter a Viewing YouTube URL")
question = st.text_input("❓ Your Question", placeholder="Ask something about the video content")

if st.button("🔍 Get Answer", use_container_width=True):
    if video_url and question:
        st.text("Streamlit is running")
        with st.spinner("Processing..."):
            response = requests.post(
                "http://127.0.0.1:5000/ask",
                json={"video_url": video_url, "question": question})
            st.text("Get the response")
            if response.status_code == 200:
                answer = response.json().get("response", "No response available")
                st.success("✅ Answer:")
                st.info(answer)
            else:
                st.error("❌ Error retrieving response!:")
                st.write(response.json().get("error", "Unknown error"))
    else:
        st.warning("Please provide both the video link and the question!")
        
        
st.markdown("---") 
st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>© 2025 Niladri. All rights reserved.</p>", unsafe_allow_html=True)
