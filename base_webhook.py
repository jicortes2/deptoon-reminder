from flask import Flask, request
from json import loads
from os import environ
from time import sleep
from base_bot import BOT, UPDATE_QUEUE, TOKEN

URL = "{}{}".format(environ["DOMAIN"], TOKEN)

PORT = int(environ.get("PORT", 5000))
app = Flask(__name__)


@app.route("/{}".format(TOKEN), methods=["GET", "POST"])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return "OK"

@app.route("/send_reminders", methods=["POST"])
def send_reminders():
    msg = loads(request.get_json(force=True)["data"])
    BOT.sendMessage(environ["GROUP_ID"], msg["message"], parse_mode="HTML")
    return "message: {}\nstatusCode: {}".format(msg["message"], 200)



if __name__ == "__main__":
    BOT.setWebhook()
    sleep(1)
    BOT.setWebhook(URL)
    app.run(host="0.0.0.0", port=PORT)
