from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import rec

app = Flask(__name__,template_folder='template')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        movie_name = request.form['movie']
        l=rec.movie(movie_name)
        return render_template('index.html',list=l)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# s=input("enter movie name ")
# rec.movie(s)