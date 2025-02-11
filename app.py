from flask import Flask, render_template
from datetime import datetime

import subprocess

# Configure the below
PASSWORD = ''
REMOTE = ''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/power_state')
def power_state():
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g mode 22 in'])
    result = subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g read 22'])
    print(f"{datetime.now()} - power_state - {result.stdout}")
    return result.stdout

@app.route('/power_button')
def power_button():
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g mode 27 out'])
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g write 27 0'])
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g write 27 1'])
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g write 27 0'])
    print(f"{datetime.now()} - power_button")
    return "power_button"

@app.route('/reset_hold')
def reset_hold():
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g mode 17 out'])
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g write 17 1'])
    print(f"{datetime.now()} - reset_hold")
    return "reset_hold"

@app.route('/reset_release')
def reset_release():
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g mode 17 out'])
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'gpio -g write 17 0'])
    print(f"{datetime.now()} - reset_release")
    return "reset_release"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
