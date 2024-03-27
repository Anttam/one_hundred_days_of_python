from flask import Flask
from flask import render_template
import requests

posts = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
  for post in posts:
    if post['id'] == post_id:
      requested_post = post
  return render_template('post.html', post=requested_post)

if __name__ == "__main__":
  app.run()