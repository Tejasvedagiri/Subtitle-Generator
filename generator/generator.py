import logging
import pysrt
import datetime

from utils.model import load_model
from utils.time import coerce_time_to_srt_format
from utils.folder import ensure_parent_dir


logger = logging.getLogger(__name__)
logger.info("Imported generator.generator module")


def generate_subtitles(input_video_path: str, output_srt_path: str, model_name: str = "large-v3", language: str = "en") -> None:
	"""Transcribe `input_video_path` and write SRT to `output_srt_path` using `model_name`.

	This is the same helper previously defined in `main.py` moved here for reuse.
	"""
	model = load_model(model_name)

	result = model.transcribe(input_video_path, language=language)

	subs = pysrt.SubRipFile()
	for index, segment in enumerate(result["segments"]):
		start_time = datetime.timedelta(seconds=segment["start"])
		end_time = datetime.timedelta(seconds=segment["end"])
		text = segment["text"].strip()

		sub = pysrt.SubRipItem(
			index=index + 1,
			start=coerce_time_to_srt_format(start_time),
			end=coerce_time_to_srt_format(end_time),
			text=text,
		)
		subs.append(sub)

	# Ensure the output directory exists before saving
	ensure_parent_dir(output_srt_path)
	subs.save(output_srt_path, encoding="utf-8")
	logger.info("Subtitles generated: %s", output_srt_path)
