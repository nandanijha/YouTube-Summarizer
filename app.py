import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title = "YouTube Video Summarizer", page_icon=":bookmark_tabs:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_code = load_lottieurl("https://lottie.host/e60c8657-aa91-4268-9296-3aa659d31d54/eUSgTZpkHS.json")

st.write("Hi :wave: I am your YouTube Video Summarizer, Boared :disappointed_relieved: of watching in 1.75x speed ! Now you can paste the link here for quick summary :information_desk_person:")
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and provide the important points also list down the links used in video
within 500 words. Please provide the summary of the text given here:  """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.write("##")
   
st.write("---")
st.title("YouTube Video to Summary :point_down:")
st.write("---")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)


    
if st.button("Get Summary "):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Key Points:")
        st.write(summary)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_code = load_lottieurl("https://lottie.host/e60c8657-aa91-4268-9296-3aa659d31d54/eUSgTZpkHS.json")


st.lottie(lottie_code,height=250,key="hello")

