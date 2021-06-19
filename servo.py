from evdev import InputDevice, list_devices, ecodes
from gpiozero import Servo
import time

servo = Servo(17)
servo.mid()

# create object gamepad
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop():
	if event.type == ecodes.EV_ABS:
		#print(event.value)
		if event.value == 255:
			print("Right")
			servo.max()
		if event.value == 0:
			print("Left")
			servo.min()