from utils.model import load_model
import pysrt
import datetime
from utils.video import split_video_ffmpeg
from utils.time import coerce_time_to_srt_format


model = load_model("large-v3")

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
