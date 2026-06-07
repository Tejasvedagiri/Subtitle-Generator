import logging
import argparse
from generator.generator import generate_subtitles

# Configure basic logging so import-time logs from modules are visible
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)
logger.info("Imported main module")


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate SRT subtitles from a video file.")
    parser.add_argument("input", default="data/input.mp4", help="Input video path (default: data/input.mp4)")
    parser.add_argument("output", default="data/output.srt", help="Output .srt path (default: data/output.srt)")
    parser.add_argument("--model", "-m", default="large-v3", help="Model name to load (default: large-v3)")
    parser.add_argument("--language", "-l", default="en", help="Language hint for transcription (default: en)")
    return parser


if __name__ == "__main__":
    parser = _build_arg_parser()
    args = parser.parse_args()
    generate_subtitles(args.input, args.output, args.model, args.language)

