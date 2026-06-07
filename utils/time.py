import logging
from pysrt import SubRipTime

logger = logging.getLogger(__name__)
logger.info("Imported utils.time module")


def coerce_time_to_srt_format(td):
    """
    Converts time in seconds to SRT time format (HH:MM:SS,mmm).
    """
    hours = td.seconds // 3600
    minutes = (td.seconds // 60) % 60
    seconds = td.seconds % 60
    milliseconds = td.microseconds // 1000

    srt_time = SubRipTime(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
    return srt_time  