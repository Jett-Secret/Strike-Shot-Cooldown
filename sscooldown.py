from pynput.keyboard import Key, KeyCode,Listener
from pynput.mouse import Button,Listener as mListener
from settingsLoader import loadSettings
import sys,datetime,time
import threading
from tkinter import Tk, Text,Label,StringVar,Button as Btn
def printHelp():
	print("help!!!")
def logFormatKey(key):
	return str(datetime.datetime.now())+" :: "+str(key)
def logFormatMouse(key,pressed):
	return str(datetime.datetime.now())+" :: "+str(key) + " :: " +str(pressed)
args = sys.argv
settings_path = "./settings.json"
if(len(args)>2):
	print("Too many arguments")
	quit()
if len(args)==2:
	if args[1]=="-h" or args[1]=="--help":
		printHelp()
	else:
		settings_path=args[1]
argssettings,code = loadSettings(settings_path)
if(code == 1):
	print("Could not load from file "+settings_path+ " but default settings were loaded.")
	while True:
		print("Would you like to continue with those settings?")
	
		inp = input("Enter Y for yes, N for no, or V to see the settings")[0].lower()
		if(inp == "y"):
			break
		elif inp == "n":
			quit()
		elif inp == "v":
			print("\n# Default Settings: #")
			for k in argssettings:
				print(k+" : "+str(argssettings[k]))
			print()
		else:
			print("I did not understand that.  Try again.\n")
elif code == -1:
	print("Could not load settings file or default settings // -1")
	quit()
	
def parseSettings(settings):
	sm_=settings["strike_mouse"].lower()
	sm = Button.left
	if sm_=="right":
		sm = Button.right
	elif sm_=="middle":
		sm = Button.middle
		
	sk_=settings["strike_key"].lower()
	sk = sk_
			
	cdk_=settings["key_to_force_cooldown"].lower()
	#print(cdk_)
	cdk=None
	try:
		cdk = Key.from_char(cdk_)
		#print(cdk)
	except:
		cdk=cdk_
		#print(cdk)
	if sm_=="right":
		sm = Button.right
	elif sm_=="middle":
		sm = Button.middle
	settings["strike_key"],settings["strike_mouse"]
	return settings["log_to_file"],settings["log_to_console"],settings["mouse_on_release"],settings["key_on_release"],settings["mouse_on_press"],settings["key_on_press"],str(sk),str(sm),str(cdk),settings["on_cooldown_color"],settings["available_color"]
def turnOff():
	global label
	label.config(bg=cdc);
def turnOn():
	global label
	label.config(bg=avc);
global lasttime
global label
lasttime = time.time();
def resetTime(force=False):
	global lasttime
	t = time.time()
	if(t-lasttime>=11 or force):
		lasttime = time.time()
	#print(time)
def desetTime(force=False):
	global lasttime
	lasttime = time.time() - 11
global ison
ison = True
def decrement_label():
	global labeltext
	global ison
	global label
	t = time.time()
	dif=11-(t-lasttime)
	if(dif<=0 and not ison):
		ison=True
		turnOn()
	elif (dif>0 and ison):
		ison=False
		turnOff()
		
	labeltext.set(str(max(0,int(dif+0.5))))
	label.config(text=labeltext.get())
	root.after(200, decrement_label )
	
	
def display():
	root.after(200, decrement_label )
ltf,ltc,mor,kor,mop,kop,sk,sm,cdk,cdc,avc = parseSettings(argssettings)
#print(cdk)
logfilepath = "./logs.txt"
fr = None

if ltf:
	fr = open(logfilepath,"a+")

def on_press(key):
	if not kop: return;
	if(ltf and fr is not None):
		fr.write(logFormatKey(key)+"\n")
		fr.flush();
	if(ltc):
		print(logFormatKey(key))
	if hasattr(key, 'vk'):	
		if key.char==sk:
			resetTime()
		if key.char == cdk:
			desetTime()
		pass#print(key)
	else:
		k = str(key)
		if k.startswith("Key."):
			k=k[4:]
		#print(str(k))
		if str(k)==sk:
			resetTime()
		if str(k) == cdk:
			desetTime()
		pass#print(key)
	
def on_release(key):
	if not kor: return;
	if(ltf and fr is not None):
		fr.write(logFormatKey(key)+"\n")
		fr.flush();
	if(ltc):
		print(logFormatKey(key))
	#print(key)
	
def on_click(x, y, button, pressed):
	if pressed and not mop:
		return
	if not pressed and not mor:
		return;
	if(ltf and fr is not None):
		fr.write(logFormatMouse(button,pressed)+"\n")
		fr.flush();
	if(ltc):
		print(logFormatMouse(button,pressed))
	if(sm==str(button)):
		resetTime()
	
root = Tk()
global movable
movable=False
def setmovable(e):
	global movable
	#print("hello!")
	movable=not movable
	root.resizable(movable, False)
	root.overrideredirect(not movable)

global label
global labeltext
labeltext = StringVar()
label =None
def run():
	global labeltext
	global label
	keyboard_listener = Listener(on_press=on_press, on_release=on_release)
	mouse_listener = mListener(on_click=on_click)

	lasttime = time.time();
	keyboard_listener.start()
	mouse_listener.start()

	root.resizable(False, False)
	root.overrideredirect(True)
	#root.geometry("48x48")
	root.title("Text Widget Example")
	#root.columnconfigure(0, weight=4)
	#root.columnconfigure(1, weight=1)
	#root.columnconfigure(1, weight=20)
	label = Label(root,text=labeltext, bg='gray',font=("Courier", 20))
	#button = Btn(root,text="X",command=lambda: root.quit())
	#button2 = Btn(root,text="border",command=setmovable)
	#button2.grid(column=0, row=0)
	#button.grid(column=1, row=0)
	label.grid(column=0, row=0)
	label.bind("<Button-1>",setmovable)
	#button.pack()
	#label.pack(ipadx=20, ipady=10)
	root.configure(bg='white')
	root.wm_attributes("-topmost", True)
	root.attributes('-toolwindow', True)
	root.wm_attributes("-transparentcolor", "white")
	
	x = threading.Thread(target=display)


	x.start()
	
	root.mainloop()
	#print("here")
		
	quit()
run()