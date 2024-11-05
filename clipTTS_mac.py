import os
import subprocess
from TTS.api import TTS
import pyperclip

def text_to_speech_from_clipboard():
    # Get text from clipboard using pyperclip for macOS compatibility
    try:
        text = pyperclip.paste()
        if not text:
            print("Clipboard is empty. Please copy some text to convert.")
            return
    except Exception as e:
        print(f"Failed to read from clipboard: {e}")
        return

    # Initialize TTS with a German model and HiFi-GAN vocoder
    tts = TTS(
        model_name="tts_models/de/thorsten/tacotron2-DDC",
        progress_bar=True,
        gpu=False  # Set to False for macOS unless you have GPU support
    )

    # Set output filename
    filename = "clipboard_tts.wav"

    # Generate the audio from text and save to file
    tts.tts_to_file(text=text, file_path=filename)

    # Play the audio file with a macOS-compatible command
    os.system(f"afplay {filename}")

    # Optional: delete the file after playing
    os.remove(filename)

if __name__ == "__main__":
    text_to_speech_from_clipboard()
