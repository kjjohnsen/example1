# This program is an example
import time
file = open("res/time.txt","w")
file.write(f"The program was last run at {time.ctime()}")
