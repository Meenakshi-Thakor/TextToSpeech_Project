import streamlit as st
from gtts import gTTS
import os
import uuid

st.set_page_config(page_title="Text to Speech", layout="centered")
st.title("🗣️ Text to Speech App (Indian English Accent)")

# User input text
text = st.text_area("Enter text to convert into speech:")

if st.button("Convert"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text!")
    else:
        # Unique filename for each run
        filename = f"speech_{uuid.uuid4().hex[:8]}.mp3"

        # Convert text to speech
        tts = gTTS(text=text, lang="en", tld="co.in")  # Indian English accent
        tts.save(filename)

        # Play audio
        audio_file = open(filename, "rb")
        st.audio(audio_file.read(), format="audio/mp3")

        # Download option
        with open(filename, "rb") as f:
            st.download_button("Download MP3", f, file_name=filename, mime="audio/mp3")

        st.success("✅ Speech generated successfully!")
