import os
from moviepy.editor import VideoFileClip
from moviepy.editor import *
from moviepy import *

video_clip = VideoFileClip('Tom.mp4')

video_clip.resize((640,360))
resized = video_clip.resize(width=360)

video_path = os.path.join('output-1.mp4')
resized.write_videofile(video_path, temp_audiofile='output-1.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
