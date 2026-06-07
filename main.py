import whisper
import pysrt
import datetime
from pysrt import SubRipTime
import subprocess


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
    print(f"Saved: {output_file}")

# Example Usage


# 1. Load the AI model (Choose from: tiny, base, small, medium, large)
# 'large-v3' is highly recommended for best accuracy with Japanese kanji and kana
model = whisper.load_model("large-v3")

# 2. Transcribe the video (Specify Japanese language for better targeting)
video_path = "data/input.mp4"

# split_video_ffmpeg(video_path, "00:00:00", "00:10:00", "output_clip.mp4")
# output_clip_path = "output_clip.mp4"

result = model.transcribe(video_path, language="en")

# 3. Create an empty SRT file structure
subs = pysrt.SubRipFile()

# 4. Process segments and add to SRT
for index, segment in enumerate(result["segments"]):
    # Convert start and end times to timedelta objects
    start_time = datetime.timedelta(seconds=segment['start'])
    end_time = datetime.timedelta(seconds=segment['end'])
    text = segment['text'].strip()

    # Create the subtitle object
    sub = pysrt.SubRipItem(
        index=index + 1,
        start=coerce_time_to_srt_format(start_time),
        end=coerce_time_to_srt_format(end_time),
        text=text
    )
    subs.append(sub)

# 5. Save the subtitles
subs.save("output.srt", encoding="utf-8")
print("Subtitles Generated Successfully!")
