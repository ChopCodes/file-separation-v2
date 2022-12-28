import sys
import time
import random

import os
import shutil
from loading import *

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/user/Downloads"
to_dir = "C:/Users/user/Downloads/sorted-files"

if os.path.exists(to_dir) == False:
    os.makedirs(to_dir)
    print("From now on, All your files in downloads folder will be sorted in "+to_dir)


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)

        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                # filename with extension is the basename eg. image.png
                p1 = from_dir + '/' + file_name
                p2 = to_dir + '/' + key
                p3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(p2):
                    if os.path.exists(p1):
                        print("Directory Exists (Test1 Check)")
                        print("Moving "+file_name)
                        shutil.move(p1, p3)
                        time.sleep(1)
                    else:
                        continue

                else:
                    if os.path.exists(p1):
                        print("Directory Exists (Test1.1 Check)")
                        os.makedirs(p2)
                        print("Moving "+file_name)
                        shutil.move(p1, p3)
                        time.sleep(1)
                    else:
                        continue

       # print(event)
       # print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()
# event_handler is the object of our class FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)
# recursive = true; refers to handling the subfolders' files as well as the files in the from_dir


# Start the Observer
observer.start()

print("Your logs will be shown in the terminal itself")
print("Made by Chop_Codes")
print("www.github.com/chopcodes")
print("chopcodes/file-separation-v2")

