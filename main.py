from codecs import IncrementalDecoder
from flask import Flask
from flask import render_template, session, request, redirect, g, url_for 
import pickle
import os


app = Flask(__name__)

app.secret_key = os.urandom(24)



########## index page ############
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


########## about page ############
@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')




########## results page ############
@app.route('/results', methods=['POST', 'GET'])
def results():
    return render_template('results.html')



    
########## courseProject page ############
@app.route('/courseProject', methods=['POST', 'GET'])
def courseProject():
    return render_template('courseProject.html')



########## thesis page ############
@app.route('/thesis', methods=['POST', 'GET'])
def thesis():
    return render_template('thesis.html')





########## publication page ############
@app.route('/publication', methods=['POST', 'GET'])
def publication():
    return render_template('publication.html')





########## experience page ############
@app.route('/experience', methods=['POST', 'GET'])
def experience():
    return render_template('experience.html')


########## skill page ############
@app.route('/skill', methods=['POST', 'GET'])
def skill():
    return render_template('skill.html')


########## certification page ############
@app.route('/certification', methods=['POST', 'GET'])
def certification():
    return render_template('certification.html')





if __name__ == '__main__':
    app.run(debug=True)