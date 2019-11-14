# Демо прогрессбара. Запускать в системной консоли
# ( не IDE )

import progressbar
import time

# вывод прогрессбара с кастомным отображением
pbar = progressbar.ProgressBar(
	widgets=[progressbar.Bar(fill='-', marker='|'), progressbar.Percentage(), ' ', progressbar.SimpleProgress()])

for i in pbar(range(50)):
	time.sleep(0.1)

pbar = progressbar.ProgressBar(widgets=[progressbar.Bar(fill=' ', marker='.', fill_left=False)]).start()
for i in range(100):
	time.sleep(0.1)
	pbar.update(i + 1)

pbar.finish()
