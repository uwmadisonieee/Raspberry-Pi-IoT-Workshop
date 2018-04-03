
from flask import Flask
import RPi.GPIO as GPIO

# Setup LED
LED = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

# Sets our server as 'app'
app = Flask(__name__)

# Creates route for LED
@app.route('/LED/<int:status>')
def index(status):
    if status == 0:
		GPIO.output(LED, GPIO.LOW)
	elif status == 1:
		GPIO.output(LED, GPIO.HIGH)

    return 'LED Light status set to: ' + str(status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')