# Diary

A voice-dictated diary tool that transcribes your speech to markdown files using Whisper, with optional AI enhancement via Ollama.

## Features

- **Voice Recording**: Record your diary entries via microphone
- **Speech-to-Text**: Transcribes audio using OpenAI Whisper (runs locally/offline)
- **AI Enhancement**: Optionally improve grammar while preserving your original tone using Ollama
- **Local Storage**: Saves entries as markdown files in `~/diary/`

## Installation

```bash
cd /path/to/diary
uv sync
```

## Usage

### Basic Recording

```bash
uv run diary dictate
```

Records audio (up to 5 minutes by default) and saves to `~/diary/YYYY-MM-DD.md`.

### Options

| Option | Description |
|--------|-------------|
| `--duration` | Recording duration in seconds (default: 300) |
| `--enhance` | Pass transcript through Ollama for grammar fixes |
| `--path` | Directory to save diary entries (default: ~/diary) |

### Examples

```bash
# 2 minute recording
uv run diary dictate --duration 120

# With AI enhancement (requires Ollama running)
uv run diary dictate --enhance

# Save to custom directory
uv run diary dictate --path /path/to/my/diary

# 1 minute with enhancement
uv run diary dictate --duration 60 --enhance
```

## Dependencies

### Required

- **uv** - Package manager
- **Whisper** - Speech-to-text (installed via `uv sync`)
- **sounddevice** - Audio recording

### Optional

- **Ollama** - Required only for `--enhance` flag
  - Must be installed and running locally
  - Requires `llama3.2` model: `ollama pull llama3.2`

## Output

Diary entries are saved to `~/diary/` with filename format `YYYY-MM-DD.md`:

```markdown
# Diary Entry — April 21, 2026

Your transcribed text here...
```

## Configuration

| Path | Purpose |
|------|---------|
| `~/.config/diary/token.pickle` | Cached OAuth token (if re-added) |
| `~/.config/diary/recording.wav` | Temporary audio recording |
| `~/diary/` | Your diary entries |