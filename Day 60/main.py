from flask import Flask, render_template, request
import requests
import dotenv
import os
import smtplib

dotenv.load_dotenv()
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')




posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

def sendmail( subject, message):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
      from_addr=email, 
      to_addrs=email, 
      msg=f"Subject:{subject}\n\n{message}"
      )


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        message= f"""
        New message from {request.form['name']}:

        {request.form['message']}

        You can reach {request.form['name']} with the following contact information:
        {request.form['email']}
        {request.form['phone']}
"""
        sendmail('New message from Contact form', message)
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    return 'hello'

if __name__ == "__main__":
    app.run()
