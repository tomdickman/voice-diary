import whisper
import sounddevice as sd
import scipy.io.wavfile as wavfile
from pathlib import Path
import numpy as np
from datetime import date

AUDIO_PATH = Path.home() / ".config" / "diary" / "recording.wav"
DIARY_PATH = Path.home() / "diary"
SAMPLE_RATE = 16000


def load_model():
    return whisper.load_model("base")


def record_audio(duration: float = 300) -> None:
    print(f"Recording... Speak your diary entry.")
    print(f"Recording for up to {duration}s. Press Ctrl+C to stop.")
    print("-" * 50)

    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    try:
        sd.wait()
    except KeyboardInterrupt:
        sd.stop()
        print("Recording stopped.")

    audio = (audio * 32767).astype(np.int16)
    AUDIO_PATH.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(AUDIO_PATH, SAMPLE_RATE, audio)
    print("Recording complete.")


def transcribe(model) -> str:
    print("Transcribing...")
    result = model.transcribe(str(AUDIO_PATH), language="en")
    return result["text"]


def format_diary(text: str) -> str:
    today = date.today()
    formatted = f"# Diary Entry — {today.strftime('%B %d, %Y')}\n\n"
    formatted += text.strip() + "\n"
    return formatted


def save_diary(text: str) -> Path:
    DIARY_PATH.mkdir(parents=True, exist_ok=True)
    today = date.today()
    file_name = f"{today.isoformat()}.md"
    file_path = DIARY_PATH / file_name
    file_path.write_text(text.strip() + "\n")
    return file_path


def process_diary(enhance: bool = False) -> Path:
    model = load_model()
    record_audio()
    text = transcribe(model)

    if enhance:
        from .enhancer import enhance_diary

        print("Enhancing with AI...")
        text = enhance_diary(text)

    diary = format_diary(text)
    path = save_diary(diary)
    return path
