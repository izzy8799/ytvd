from pytube import YouTube
import os, time, os.path
from os import path
import zenipy
from subprocess import Popen
user_folder=os.path.expanduser('~')
def check_ytvd_folder():
	if str(path.exists(f"{user_folder}/YTVD")):
		try:
			os.chdir(f"{user_folder}/YTVD")
		except:
			os.mkdir(f"{user_folder}/YTVD")
			os.chdir(f"{user_folder}/YTVD")
			main()
		else:
			main()
def main():
	link=zenipy.zenipy.entry(text='Insert the link to the video...', placeholder='', title='YTVD', width=330, height=120, timeout=None)
	try:
		loading = Popen(["zenity", "--progress", "--pulsate", "--no-cancel", "--auto-close", "--title", "YTVD", "--text", "Downloading..."])
		YouTube(link).streams.get_highest_resolution().download()
	except:
		loading.terminate()
		zenipy.zenipy.error(title='YTVD', text='Failed to download video', width=330, height=120, timeout=None)
	else:
		loading.terminate()
		zenipy.zenipy.message(title='YTVD', text='Video downloaded successfully!', width=330, height=120, timeout=None)

check_ytvd_folder()
