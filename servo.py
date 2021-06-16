import RPi.GPIO as GPIO
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

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17,50)
p.start(7.50)
angle = 0.3
my = 7.5 
try:
	while True:
		char = screen.getch()
		if char == ord('q'): 
			break
		if char == curses.KEY_RIGHT:
			print("Right Key pressed")
			my += 1.0
			p.ChangeDutyCycle(my)
			time.sleep(1)
			
		if char == curses.KEY_LEFT:
			print("Left Key pressed")
			my -= 1.0
			p.ChangeDutyCycle(12.5)
			
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
		
    p.stop()	
    GPIO.cleanup()