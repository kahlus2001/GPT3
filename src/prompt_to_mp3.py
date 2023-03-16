import os

import vlc
import openai
from gtts import gTTS
import time
import playsound

# Set up OpenAI API credentials
openai.api_key = os.getenv("MY_API_KEY")
# Set up gTTS language
language = "en"

# Send prompt to OpenAI API and get response
prompt = "How to wake up early?."
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)

# Get text response from OpenAI and create audio file using gTTS
text_response = response.choices[0].text.strip()
audio_file = "gpt_response.mp3"

text_to_audio = "Prompt: " + prompt + " Response: " + text_response
tts = gTTS(text=text_to_audio, lang=language)
tts.save(audio_file)

# Play audio file using playsound library
playsound.playsound("gpt_response.mp3")
