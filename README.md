# AI Video Q&A

An AI-powered web application that allows users to ask questions about the content of YouTube videos. The application extracts and processes the video transcript to provide context-aware answers using advanced natural language processing techniques.


## Features

- 📹 **YouTube Video Processing**: Extracts transcript data from YouTube videos.
- 🤖 **AI-Powered Q&A**: Uses Google's Gemini AI to provide context-based answers.
- 🌍 **Web Interface**: Simple and intuitive UI built with Streamlit.
- 🚀 **Fast & Efficient**: Processes videos and returns responses in real-time.

## Tech Stack

- **Backend**: Flask, LangChain, NLTK, ChromaDB, Google Gemini AI
- **Frontend**: Streamlit
- **APIs**: YouTube Data API, Google AI Services

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip

### Steps

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/LLM-YouTube-Video-QnA.git
   cd LLM-YouTube-Video-QnA
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Backend (Flask App)**
   ```sh
   python q&a.py
   ```

4. **Run the Frontend (Streamlit App)**
   ```sh
   streamlit run ui.py
   ```

## Usage

1. Open the Streamlit app in your browser.
2. Enter a YouTube video URL.
3. Type a question related to the video content.
4. Click **Get Answer** and receive an AI-generated response.

## API Endpoint

- **POST `/ask`**: Process a video and return an AI-generated answer.
  - **Request Body**:
    ```json
    {
      "video_url": "https://www.youtube.com/watch?v=example",
      "question": "What is the main topic of this video?"
    }
    ```
  - **Response**:
    ```json
    {
      "response": "The video discusses the fundamentals of AI."
    }
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

👤 **Niladri**  
© 2025 Niladri. All rights reserved.

