from flask import Flask, send_from_directory
import RPi.GPIO as GPIO

# Setup LED
LED = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

app = Flask(__name__, static_url_path="")
app._static_folder = "static"

# Creates route for LED
@app.route('/LED/<int:status>')
def led(status):
    if status == 0:
	GPIO.output(LED, GPIO.LOW)
    elif status == 1:
	GPIO.output(LED, GPIO.HIGH)

    return 'LED Light status set to: ' + str(status)

@app.route('/')
def root():
	return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
