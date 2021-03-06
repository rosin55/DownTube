# Скрипт для скачивания роликов с Ютуба
# 01.11.2019
# использует pytube Version: 9.5.2
# с коррекцией  return self.player_config_args['title'] в pytube\__main__.py

from pytube import YouTube
# URL для отладки
# https://www.youtube.com/watch?v=pGQGVJdDO7U


def progress_function(selth, chunk, file_handler, bytes_remaining):
	''' пп вызывается в процессе загрузки и печатает процент загруженного '''
	p = round((1-bytes_remaining/video.filesize)*100, 4)
#	print ('осталось байт {:10.0f}'.format(bytes_remaining))
	ostatok = p % 10
	if ostatok < 0.01:
		print('\rосталось {:.2%}'.format(bytes_remaining/video.filesize))


video_link = input('1. Задайте URL скачиваемого видео ')
yt = YouTube(url=video_link, on_progress_callback=progress_function)
print('Имя файла = ', yt.title)
for st in yt.streams.filter(progressive=True, file_extension='mp4').all():
	print(st.itag, st.mime_type, st.resolution)
video = yt.streams.filter(progressive=True, file_extension='mp4').first()
print('Размер файла = ', video.filesize//1000000, ' Mb')
video.download('c:/temp')
