from flask import Flask, send_from_directory
import os

app = Flask(__name__)
server = app.server
@app.route('/WW_verify_3lX7NSa3vJ4Rt4QX.txt')
def verify():
    return send_from_directory(os.getcwd(), 'WW_verify_3lX7NSa3vJ4Rt4QX.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
