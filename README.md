# Subtitle-Generator

Generate SRT subtitle files from video using Whisper-style transcription models.

## Features
- Transcribe video files and produce `.srt` subtitle files.
- Uses OpenAI Whisper models for transcription.

## Quick Start

### Step 1: Install CUDA
CUDA is required for GPU acceleration. Download and install from:
https://developer.nvidia.com/cuda-downloads

### Step 2: Install UV
UV is a fast Python package installer. Install it using:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or see the official documentation: https://docs.astral.sh/uv/

### Step 3: Sync Dependencies
Run `uv sync` to install all project dependencies:

```bash
uv sync
```

### Step 4: Run on Sample Video
Test the setup by running on a sample video:

```bash
uv run convert --help
```

Then run the conversion:

```bash
uv run convert data/sample.mp4 data/sample.srt
```

## Usage

```bash
uv run convert --help
```

**Output:**
```
usage: convert [-h] [--model MODEL] [--language LANGUAGE] input output

Generate SRT subtitles from a video file.

positional arguments:
  input                 Input video path (default: data/input.mp4)
  output                Output .srt path (default: data/output.srt)

options:
  -h, --help            show this help message and exit
  --model MODEL, -m MODEL
                        Model name to load (default: large-v3)
  --language LANGUAGE, -l LANGUAGE
                        Language hint for transcription (default: en)
```

**Examples:**
```bash
# Uses default paths (data/input.mp4 → data/output.srt)
uv run convert

# Specify custom input and output paths
uv run convert video.mp4 subtitles.srt

# Specify model and language
uv run convert video.mp4 subtitles.srt --model large-v3 --language en

# Using short flags
uv run convert video.mp4 subtitles.srt -m base -l es
```

## Notes
- The implementation uses the OpenAI Whisper project for model loading and transcription. See the upstream repository for model details and options: https://github.com/openai/whisper
- Output directories are created automatically when needed.
- Supported languages depend on the Whisper model being used.
- For sample videos to test with, check the TalkVid dataset on HuggingFace: https://huggingface.co/datasets/FreedomIntelligence/TalkVid

## License
This project inherits the license declared in the repository.
