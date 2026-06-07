import subprocess
import logging


logger = logging.getLogger(__name__)
logger.info("Imported utils.video module")

def split_video_ffmpeg(input_file, start_time, end_time, output_file):
    """
    Splits a video clip from start_time to end_time without re-encoding.
    Times can be in seconds (e.g., 90) or 'HH:MM:SS' format.
    """
    command = [
        'ffmpeg', '-ss', str(start_time), 
        '-i', input_file, 
        '-to', str(end_time), 
        '-c', 'copy', output_file
    ]
    
    # Run the command
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info(f"Saved: {output_file}")
