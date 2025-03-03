from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, WeChat API Verify!"

@app.route("/WW_verify_3lX7NSa3vJ4Rt4QX.txt")
def wechat_verify():
    return send_from_directory("static", "WW_verify_3lX7NSa3vJ4Rt4QX.txt")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
