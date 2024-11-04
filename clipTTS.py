import os
import subprocess
from TTS.api import TTS

def text_to_speech_from_clipboard():
    # Get text from clipboard using xclip
    try:
        text = subprocess.check_output("xclip -selection clipboard -o", shell=True).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        print("Failed to read from clipboard. Ensure you have text copied.")
        return

    if not text:
        print("Clipboard is empty. Please copy some text to convert.")
        return

    # Initialize TTS with a German model and HiFi-GAN vocoder
    tts = TTS(
        model_name="tts_models/de/thorsten/tacotron2-DDC",
        progress_bar=True,
        gpu=True
    )

    # Set output filename
    filename = "clipboard_tts.wav"

    # Generate the audio from text and save to file
    tts.tts_to_file(text=text, file_path=filename)

    # Play the audio file
    os.system(f"mpv {filename}")

    # Optional: delete the file after playing
    os.remove(filename)

if __name__ == "__main__":
    text_to_speech_from_clipboard()
