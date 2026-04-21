import ollama
from datetime import date

MODEL = "llama3.2"


def enhance_diary(raw_text: str) -> str:
    today = date.today()
    prompt = f"""You are helping edit a voice-to-text diary entry.

The original transcription may have grammar errors, filler words, or awkward phrasing from speech-to-text.

Your task:
1. Fix only grammar and spelling errors
2. Do NOT change the tone or style - preserve exactly how the original sounds
3. Do NOT add any text stating this has been edited or enhanced
4. Keep the exact same voice and style as the original

Today's date: {today.strftime("%B %d, %Y")}

Original transcription:
{raw_text}

Edited diary entry:"""

    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
