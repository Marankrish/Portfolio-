from flask import Flask,render_template,request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__,static_folder="static")


@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Send the data via email
        send_email(name, email, message)

        return "<h1>Thank you for your message! I'll get back to you soon.</h1>"

    return render_template("index.html")  # Your contact form page

def send_email(name, email, message):
    # Replace with your email settings
    sender_email = "marankrishnakumar@gmail.com"
    receiver_email = "marankrishnakumar@gmail.com"
    password = "hvvs lppf zfog ctfy"  # For Gmail, use App Passwords for better security

    msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg["Subject"] = "New Contact Form Submission"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Set up the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug = True)