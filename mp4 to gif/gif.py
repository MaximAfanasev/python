#для работы модуль editor (может работать с субтитрами)
from moviepy.editor import VideoFileClip

# обращаемся к классу VideoFileClip
videoClip = VideoFileClip("my_video.mp4")

videoClip.write_gif("my_video.gif")
