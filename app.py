from flask import Flask , render_template,  request
import pandas as pd
from flask_bootstrap import Bootstrap
from forms import ContactForm
from flask_mail import Mail, Message
import os
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = os.urandom(24)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
   
}

mail = Mail(app)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/instalaciones")
def instalaciones():
    return render_template("instalaciones.html")

@app.route('/contacto', methods=["GET", "POST"])
def contacto():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email, 'subject': subject, 'message': message}, index=[0])
        #res.to_csv('./contactusMessage.csv')
        msg = Message('Hello', sender = email, recipients = ['test.mail.protocol.lm@gmail.com'])
        msg.body = res
        mail.send(msg)
        return render_template('contacto.html', form=form)
    else:
        return render_template('contacto.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)


    # if the the server is already used
# sudo lsof -i :5000  to detect the process listening on the port

# and then sudo kill -9 <process_id>