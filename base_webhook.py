from flask import Flask, request
from json import loads
from os import environ
from time import sleep
from base_bot import BOT, UPDATE_QUEUE, TOKEN
from db import find_reminders

URL = "{}{}".format(environ["DOMAIN"], TOKEN)

PORT = int(environ.get("PORT", 5000))
app = Flask(__name__)


@app.route("/{}".format(TOKEN), methods=["GET", "POST"])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return "OK"

@app.route("/send_reminders", methods=["POST"])
def send_reminders():
    tuples = find_reminders()
    for tup in tuples:
        BOT.sendMessage(tup["chat_id"], tup["reminder"], parse_mode="HTML")
    return "message: {}\nstatusCode: {}".format(msg["message"], 200)



if __name__ == "__main__":
    BOT.setWebhook()
    sleep(1)
    BOT.setWebhook(URL)
    app.run(host="0.0.0.0", port=PORT)
