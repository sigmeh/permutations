#!/usr/bin/env python
import subprocess,time
def main():
	subprocess.Popen(['python ./server.py &'],shell=True)#check for running server/start server
	time.sleep(1)
	subprocess.Popen(['open http://localhost:8000/perm'],shell=True)
if __name__ == '__main__':
	main()