import socket
from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
        return ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])



if __name__ == "__main__":
            port = int(os.environ.get('PORT', 5000))
            app.run(debug=True, host='0.0.0.0', port=port)
~                                                          
