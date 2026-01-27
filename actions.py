import pyautogui
import os

screen_w, screen_h = pyautogui.size()

def move_cursor(index_finger):
    x = int(index_finger.x * screen_w)
    y = int(index_finger.y * screen_h)
    pyautogui.moveTo(x, y)

def pinch_distance(finger1, finger2):
    return abs(finger1.x - finger2.x) + abs(finger1.y - finger2.y)

def click_if_index_pinch(index, thumb):
    if index is None or thumb is None:
        return False

    if pinch_distance(index, thumb) < 0.03:
        pyautogui.click()
        return True

    return False

def command_if_middle_pinch(middle, thumb):
    if middle is None or thumb is None:
        return False

    if pinch_distance(middle, thumb) < 0.03:
        return True

    return False


def handle_command(command):
    if "open chrome" in command:
        os.startfile(r"...")#File Path Here
    if "open games" in command:
        os.startfile(r"...")#File Path Here
