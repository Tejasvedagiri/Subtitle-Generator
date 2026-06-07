import logging
import argparse
from generator.generator import generate_subtitles
from utils.input import collect_video_input_paths, output_srt_path_for_input
from utils.model import load_model

# Configure basic logging so import-time logs from modules are visible
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)
logger.info("Imported main module")


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate SRT subtitles from video files or directories.")
    parser.add_argument(
        "inputs",
        nargs="+",
        help="One or more input video files or directories containing video files.",
    )
    parser.add_argument("--model", "-m", default="large-v3", help="Model name to load (default: large-v3)")
    parser.add_argument("--language", "-l", default="en", help="Language hint for transcription (default: en)")
    return parser


def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    input_paths = collect_video_input_paths(args.inputs)
    if not input_paths:
        parser.error("No supported video files found in the provided inputs.")

    model = load_model(args.model)
    for input_path in input_paths:
        generate_subtitles(
            input_path,
            output_srt_path_for_input(input_path),
            args.model,
            args.language,
            model=model,
        )

if __name__ == "__main__":
    main()