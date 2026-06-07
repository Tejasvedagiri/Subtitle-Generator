import logging
import os

logger = logging.getLogger(__name__)
logger.info("Imported utils.input module")

SUPPORTED_VIDEO_EXTENSIONS = (
    ".mp4",
    ".mov",
    ".mkv",
    ".avi",
    ".flv",
    ".wmv",
    ".webm",
    ".mp3",
    ".wav",
)


def is_supported_video_file(path: str) -> bool:
    """Return True if the path is an existing file with a supported video/audio extension."""
    if not os.path.isfile(path):
        return False
    _, ext = os.path.splitext(path)
    return ext.lower() in SUPPORTED_VIDEO_EXTENSIONS


def output_srt_path_for_input(input_video_path: str) -> str:
    """Return the output .srt path for the given input video path."""
    base, _ = os.path.splitext(input_video_path)
    return f"{base}.srt"


def collect_video_input_paths(inputs):
    """Expand input files and directories into a list of supported video file paths."""
    resolved_paths = []

    for input_path in inputs:
        if os.path.isdir(input_path):
            for root, _, files in os.walk(input_path):
                for filename in sorted(files):
                    candidate = os.path.join(root, filename)
                    if is_supported_video_file(candidate):
                        resolved_paths.append(candidate)
        elif os.path.isfile(input_path):
            if is_supported_video_file(input_path):
                resolved_paths.append(input_path)
            else:
                logger.warning("Skipping unsupported input file: %s", input_path)
        else:
            logger.warning("Skipping missing input path: %s", input_path)

    # Preserve input order and remove duplicates
    seen = set()
    ordered_paths = []
    for path in resolved_paths:
        if path not in seen:
            seen.add(path)
            ordered_paths.append(path)

    return ordered_paths
