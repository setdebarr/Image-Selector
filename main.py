"""
Created on Tues June 23.

@author: Sean DeBarr

"""
import os
import platform
import time
import shutil
import time
from alive_progress import alive_bar

PATH_INPUT = os.path.normpath(os.path.expanduser("~/Desktop/gopro"))
PATH_OUTPUT = os.path.normpath(os.path.expanduser("~/Desktop/Timelapse"))

# 24 hour format
START_TIME = 6
STOP_TIME = 17

# In minutes
TIME_BETWEEN_SHOTS = 5


def main():
    """Program will move photos from one directory to another."""
    # DON'T TOUCH!!
    COUNTER = 1
    folder = os.listdir(PATH_INPUT)
    # goes through every folder in PATH directory
    for fol in folder:
        # creates a list of all files in curently selected folder
        files = os.listdir(PATH_INPUT + "\\" + fol)
        with alive_bar(len(files), spinner="classic", bar="classic") as bar:
            # goes through every file in the currently selected folder
            for file in files:
                # check to make sure the os being used is Windows
                if platform.system() == "Windows":
                    current_file = PATH_INPUT + "\\" + fol + "\\" + file
                    # converts system time to struct_time for easy manipulation
                    creation = time.localtime(os.path.getmtime(current_file))
                    # narrows down to weekday files between specified times
                    if (
                        (creation[3] >= START_TIME)
                        and (creation[3] <= STOP_TIME)
                        and (creation[6] <= 4)
                    ):
                        # narrows down to a file every 5 minutes
                        if creation[4] % TIME_BETWEEN_SHOTS == 0:
                            # copies file to location specified in PATH_OUTPUT
                            shutil.copyfile(
                                current_file, PATH_OUTPUT + "\\" + str(COUNTER) + ".JPG"
                            )
                            COUNTER += 1
                bar()


if __name__ == "__main__":
    main()
