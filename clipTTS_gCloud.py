import os
from gtts import gTTS
import subprocess



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

    # Create TTS object with German language
    tts = gTTS(text, lang='de')

    # Save the generated audio to a file
    filename = "clipboard_tts.mp3"
    tts.save(filename)

    # Play the audio file
    os.system(f"mpv {filename}")

    # Optional: delete the file after playing
    os.remove(filename)

if __name__ == "__main__":
    text_to_speech_from_clipboard()
