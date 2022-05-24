from flask import Flask
import os
import socket   

app = Flask(__name__)


@app.route('/get_ip')
def home():
	hostname = socket.gethostname()   
	IPAddr = socket.gethostbyname(hostname)
	return f'<h1>Hostname: {hostname}\nIP Addr: {IPAddr}</h1>'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)