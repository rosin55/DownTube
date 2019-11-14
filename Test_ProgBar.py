import progressbar
import time

pbar = progressbar.ProgressBar(widgets=[progressbar.Bar(), progressbar.Percentage(), ' ', progressbar.ETA()])
for i in pbar(range(50)):
	time.sleep(0.5)