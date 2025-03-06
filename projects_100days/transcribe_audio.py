# import whisper
# import torch

# # Check if GPU is available
# device = "cuda" if torch.cuda.is_available() else "cpu"
# print(f"Running on {device}")

# # Load the model on GPU
# model = whisper.load_model("large-v3-turbo", device=device)

# # Transcribe the mp3 file
# result = model.transcribe("C:/Users/pepso/projects/python_100/projects_100days/ICT220.mp3")
# print(result["text"])


import whisper
import torch
import os

# Ensure FFmpeg is available
os.environ["PATH"] += os.pathsep + r"C:\path\to\ffmpeg\bin"

# Check if FFmpeg is detected
ffmpeg_check = os.system("ffmpeg -version")
if ffmpeg_check != 0:
    print("FFmpeg is not properly installed or not in the PATH.")
else:
    print("FFmpeg is detected!")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on {device}")

model = whisper.load_model("large-v3-turbo", device=device)

# Use the absolute path to your MP3 file
audio_path = "C:/Users/pepso/projects/python_100/projects_100days/ICT220.mp3"
result = model.transcribe(audio_path)
print(result["text"])
