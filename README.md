
# YouTube Summarizer

Welcome to the YouTube Video Summarizer! This tool helps you quickly generate summaries of YouTube videos, perfect for when you're short on time and want to grasp the key points without watching the entire video. Just paste the YouTube link, and get an instant summary!
Maximize your time and knowledge with concise summaries!

## Features

- Transcript Extraction: Automatically fetches the transcript of the given YouTube video.
- AI-Powered Summarization: Uses Google's Gemini Pro AI model to generate a concise summary of the video.
- Visual Interface: Simple and interactive UI built with Streamlit.


## How To Use

- Enter YouTube Video Link: Paste the YouTube video link in the provided text input field.
- View Video Thumbnail: The thumbnail of the video will be displayed once the link is entered.
- Get Summary: Click on the "Get Summary" button to generate the summarized content.
- View Key Points: The summary will be displayed under the "Key Points" section.
## Installation

To run this project, you need to have Python installed on your system. Follow the steps below to set up and run the project:

1. Install Python: Download and install Python from the official website.

2. Clone the repository:
```bash
  git clone https://github.com/yourusername/youtube-video-summarizer.git
  cd youtube-video-summarizer

```
3. Install dependencies:
```bash
    pip install -r requirements.txt
```
4. Set up environment variables:
Create a .env file in the project root directory and add your Google   API key:
```bash
    GOOGLE_API_KEY=your_google_api_key
```
5. Run the Streamlit app:
```bash
    streamlit run app.py

```
