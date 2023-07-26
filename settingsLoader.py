import json
def loadSettings(path):
	try:
		fr = open(path,'r')
		
		js = json.load(fr)
		print(js)
		return js,0
	except:
		s= '{"log_to_file":false,"log_to_console":false,"mouse_on_release":false,"key_on_release":false,"mouse_on_press":true,"key_on_press":true,"strike_key":"None","strike_mouse":"left","key_to_force_cooldown":"0"}'
		
		try:
			js = json.loads(s)
			return js,1
		except:
			return None,-1