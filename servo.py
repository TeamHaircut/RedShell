from gpiozero import Servo
import time 
import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

servo = Servo(17)
servo.mid()

try:
	while True:
		print(servo.value)
		char = screen.getch()
		if char == ord('q'): 
			break
		if char == curses.KEY_RIGHT:
			if servo.value != 1.0:
				print("Right Key pressed")
				servo.max()
				time.sleep(1)
			
		if char == curses.KEY_LEFT:
			if servo.value != -1.0:
				print("Left Key pressed")
				servo.min()
				time.sleep(1)

except KeyboardInterrupt:
	print("Program Terminated")
			
finally:
	# shut down cleanly
	curses.nocbreak()
	screen.keypad(False)
	curses.echo()
	curses.endwin()