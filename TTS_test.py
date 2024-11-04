from TTS.api import TTS

# Initialize the TTS model with a German voice
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=True, gpu=True)

# Define the German text
text = "Hallo! Das ist eine kurze Demonstration der Sprachsynthese auf Deutsch."

# Generate and save the audio file
tts.tts_to_file(text=text, file_path="demo_deutsch.wav")

print("Audio file 'demo_deutsch.wav' has been generated.")
