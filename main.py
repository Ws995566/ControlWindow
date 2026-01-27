from OpenCamera import get_fingers
from SpeechRecognition import listen_command
from actions import (move_cursor, click_if_index_pinch, command_if_middle_pinch, handle_command)

MODE_CURSOR = 0
MODE_COMMAND = 1
mode = MODE_CURSOR

while True:
    if mode == MODE_CURSOR:
        thumb, index, middle = get_fingers()

        if index and thumb:
            move_cursor(index)
            click_if_index_pinch(index, thumb)

        if middle and thumb:
            if command_if_middle_pinch(middle, thumb):
                mode = MODE_COMMAND

    else:
        print("Listening...")
        command = listen_command()
        print("You said:", command)
        handle_command(command)
        mode = MODE_CURSOR
