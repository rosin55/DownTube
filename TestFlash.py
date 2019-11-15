from sys import stdout
from time import sleep

for i in range(1,20):
    stdout.write("\r%2d" % i)
#    stdout.flush()
    sleep(0.5)
stdout.write("\r  \r\n") # clean up
