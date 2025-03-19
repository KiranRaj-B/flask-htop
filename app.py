from flask import Flask, render_template_string
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    #get the user admin name here
    username = os.getenv('USER') or os.getenv('USERNAME')

    #get our server time in ist
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    # now we'll render htmll here 
    return render_template_string('''
        <h1>System Information</h1>
        <p>Name: Kiran Sadashiv Badakambi</p>
        <p>Username: {{ username }}</p>
        <p>Server Time (IST): {{ server_time }}</p>
        <pre>{{ top_output }}</pre>
    ''', username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
