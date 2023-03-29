import cv2
import numpy as np
import pyautogui
import keyboard
import time
from constant import *

# Video object
FOURCC = None
OUT = None

def wait_start():
    for i in range(3):
        time.sleep(1)
        print(f'Starting auto coding in {i} seconds ...')

def delete_current_file():
    print('Deleting current file ...')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('delete')
    pyautogui.keyUp('delete')

def shot():
    global OUT
    img = pyautogui.screenshot(region=[TOP, LEFT, WIDTH, HEIGHT])
    # Convert the image to a numpy array
    frame = np.array(img)
    # Convert the image from RGB to BGR for OpenCV
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # Add the image to the video
    OUT.write(frame)

def write_code(code: str, record: bool = False):
    print('Writing the code ...')
    if not record:
        pyautogui.typewrite(code, interval=0.01)
    else:
        for index, ch in enumerate(code):
            keyboard.write(ch)
            if record:
                shot()
            # Add frames at the end of the code
            if record and len(code)-1 == index:
                for i in range(40):
                    shot()

def create_video():
    global FOURCC, OUT
    print('Creating the video ...')
    FOURCC = cv2.VideoWriter_fourcc(*'XVID')
    OUT = cv2.VideoWriter(VIDEO_NAME, FOURCC, FPS, SCREEN_SIZE)

def close_video():
    global FOURCC, OUT
    print('Closing the video ...')
    OUT.release()
    cv2.destroyAllWindows()

def auto_writter(record: bool = False):
    # Get the code from the file
    with open(FILEPATH, 'r') as file:
        print('Reading the file ...')
        code = file.read()
    if record:
        create_video()
    wait_start()
    delete_current_file()
    write_code(code, record)
    if record:
        close_video()
