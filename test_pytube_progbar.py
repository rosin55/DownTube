# -*- coding: utf-8 -*-
# в win консоли выдать chcp utf-8
# Скрипт для скачивания роликов с Ютуба
# с отображением процента загрузки через модуль progressbar
# 18.11.2019
# использует pytube Version: 9.5.2
# с коррекцией  return self.player_config_args['title'] в pytube\__main__.py

from pytube import YouTube
import progressbar

# URL для отладки
# https://www.youtube.com/watch?v=pGQGVJdDO7U

def progress_function(selth, chunk, file_handler, bytes_remaining):
	""" пп вызывается в процессе загрузки и печатает процент загруженного """
	p = round((1-bytes_remaining/video.filesize)*100, 4)
	ostatok = p % 1
	if ostatok < 0.01:
#       Отображение текущего значения прогрессбара
		pbar.update(p)


video_link = input('1. Задайте URL скачиваемого видео ')
yt = YouTube(url=video_link, on_progress_callback=progress_function)
print('Имя файла = ', yt.title)
for st in yt.streams.filter(progressive=True, file_extension='mp4').all():
	print(st.itag, st.mime_type, st.resolution)
video = yt.streams.filter(progressive=True, file_extension='mp4').first()
print('Размер файла = ', video.filesize//1000000, ' Mb')

#     Задание параметров прогрессбара
pbar = progressbar.ProgressBar(widgets=[progressbar.Bar(fill='-', marker='+', fill_left=True)]).start()
video.download('c:/temp')

