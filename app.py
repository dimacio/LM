from flask import Flask , render_template,  request
import pandas as pd
from flask_bootstrap import Bootstrap
from forms import ContactForm
from flask_mail import Mail, Message
import os
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = os.urandom(24)


app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'fabc0cf92610c9'
app.config['MAIL_PASSWORD'] = 'b9986cb14c0b16'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False



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
        msg.body = res.to_json()
        mail.send(msg)
        return render_template('contacto.html', form=form)
    else:
        return render_template('contacto.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)


    # if the the server is already used
# sudo lsof -i :5000  to detect the process listening on the port

# and then sudo kill -9 <process_id>