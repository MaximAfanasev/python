#для работы модуль editor (может работать с субтитрами)
import moviepy.editor
from а import Path

video_file = Path('my_video.mp4')
# обращаемся к классу VideoFileClip
# и передаем путь до файла
video = moviepy.editor.VideoFileClip(f'{video_file}')
# вырежем аудиодорожку из видео
audio = video.audio
#stem - обрезает формат после точки и добавляем mp3
audio.write_audiofile(f'{video_file.stem}.mp3')
