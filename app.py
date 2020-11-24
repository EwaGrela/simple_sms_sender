from flask import Flask, request, render_template, redirect, url_for
from celery import Celery
from nexmo import Sms, Client
from config import API_SECRET, API_KEY, CELERY_BROKER_URL

app = Flask(__name__)

print("app name", app.name)

celery = Celery(app.name, broker=CELERY_BROKER_URL)

sms = Sms(key=API_KEY, secret=API_SECRET)


@celery.task
def send_sms(msg_text, send_to):
    sms.send_message({
            "from": 'test',
            "to": send_to,
            "text": msg_text,
    })
    

@app.route("/sms", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        message = request.form.get("message")
        send_to = request.form.get("send_to")
        duration = request.form.get("duration")
        duration_unit = request.form.get("duration_unit")
        if not duration:
            duration = 2
        duration = int(duration)
        if not duration_unit or duration_unit == "seconds":
            duration *= 1
        elif duration_unit == "minutes":
            duration *= 60
        elif duration_unit == "hours":
            duration *= 3600        
        send_sms.apply_async(args=[message, send_to], countdown=duration)
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)