from flask import Flask, render_template_string, request   # Importing the Flask modules 
import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library

servo_pin = 17 # GPIO Pin where sero is connected
GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 50)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially
app = Flask(__name__)
#HTML Code 
TPL = '''
<html>
    <head><title>Web Page Controlled Servo</title></head>
    <body>
        <form method="POST" action="left">
            <input type="submit" value="left" />
        </form>
		<form method="POST" action="right">
            <input type="submit" value="right" />
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/left", methods=["POST"])
def left():
    # Change duty cycle
    p.ChangeDutyCycle(1.0)
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    return render_template_string(TPL)
@app.route("/right", methods=["POST"])
def right():
    # Change duty cycle
    p.ChangeDutyCycle(12.5)
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    return render_template_string(TPL)
# Run the app on the local development server
if __name__ == "__main__":
    app.run()