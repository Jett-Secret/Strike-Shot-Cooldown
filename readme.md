# About
A shitty little program I made to track the cooldown of strike shot.  This should hopefully help with the strikeshot cooldown bug.  I have not super tested this, so let me know if you notice anything.

Note, this is /technically/ a key logger.  Please don't leave it open while you do your banking, and only allow logging if you're careful and actually debugging.  You also may get a warning from an anti-virus.  If you trust me (you probably shouldn't but you know) then let it through and again, make sure you're NOT leaving it open while you use your computer normally.

# Set up
* Download this either with git or by a zip file and store it on a folder on your pc.  If saved as a zip, extract the contents somewhere
* Naviate to the folder the files are.
* Edit the settings.json file as you need, trying to get it to match your in game controls.
* Right click and open command prompt.  
* Type python ./sscooldown.py

# Settings
"log_to_file": Write all logs to a file.  You probably don't want this
"log_to_console": Write all logs to a console.  Again, you probably don't want this
"mouse_on_release": Turning this off will ignore any and all mouse button releases
"key_on_release": Turning this off will ignore any and all key releases
"mouse_on_press": Turning this off will ignore any and all mouse button presses
"key_on_press": Turning this off will ignore any and all key presses
"strike_key": The keyboard key you use to strike (eg: if you use moba controls)
"strike_mouse": Which mouse button you use to strike (probably left)
"key_to_force_cooldown": The key that when pressed will set the cooldown to zero, indicating your ss is active again.  You probably want to press this after every set.
"on_cooldown_color": The color of the background to indicate the cooldown is not available
"available_color": The color of the background to indicate the cooldown is available

Some settings may break the program.

# Errors
If you get any errors, you likely will need to install packages.  Probably want to try installing tkinter or pynput with 
```pip install pynput,tkinter```

# Notes
* clicking on the display will not click through.  Instead it will switch itself into a movable window.  Clicking again will unset this back to the undecorated default window
* because it has no sense of the game state, try not to click outside of gameplay to limit the likelihood of it become unsyncd

