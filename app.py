# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 22:09:07 2022

@author: adrie
"""


from flask import Flask, request, render_template, jsonify, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import random



app = Flask(__name__)

app.secret_key = 'capstone2'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'

mysql = MySQL(app)

from preprocessmethods import *
from ENSVM import svm, vect as vectsvm
from ENMNB import mnb, vect as vectmnb
from BMSVM import svmBM, vect as vectsvmBM
from CNSVM import svmCN, vect as vectsvmCN
from BMMNB import mnbBM, vect as vectmnbBM
from CNMNB import mnbCN, vect as vectmnbCN
 
import csv


dict_from_csv = {}

with open('response3.csv', mode = 'r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}


dict_from_csvBM = {}

with open('ResponseBM.csv', mode = 'r') as inp:
    reader = csv.reader(inp)
    dict_from_csvBM = {rows[0]: rows[1] for rows in reader}

dict_from_csvCN = {}

with open('responseCN.csv', mode = 'r', encoding='utf8', errors='ignore' ) as inp:
    reader = csv.reader(inp)
    dict_from_csvCN = {rows[0]: rows[1] for rows in reader}

bye_response = ['Thank you for contacting!', 'Have a great day!', 'Goodbye!']
greet_response = ['Hi', 'Hey there!', 'Is there anything I could help you today?']

bye_CN= ['谢谢您联络我们!', '再见!']
greet_CN = ['你好!', '欢迎!']

bye_BM = ['Terima kasih kerana menghubungi kita!', 'Terima kasih!']
greet_BM = ['Apakah saya boleh bantu?', 'Hai!']

@app.route("/home.html")
def home():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        return render_template('home.html')

@app.route("/ENSVM", methods = ['GET', 'POST'])
def ENSVM():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT bookid FROM user WHERE email = % s', (session['email'], ))
        user = cursor.fetchall()
        bookings = [item[0] for item in user]
        return render_template('ENSVM.html', bookings = bookings)

@app.route("/BMSVM", methods = ['GET', 'POST'])
def BMSVM():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT bookid FROM user WHERE email = % s', (session['email'], ))
        user = cursor.fetchall()
        bookings = [item[0] for item in user]
        return render_template('BMSVM.html', bookings = bookings)

@app.route("/CNSVM", methods = ['GET', 'POST'])
def CNSVM():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT bookid FROM user WHERE email = % s', (session['email'], ))
        user = cursor.fetchall()
        bookings = [item[0] for item in user]
        return render_template('CNSVM.html', bookings = bookings)


@app.route("/submit", methods = ['POST'])
def submit():  
        cursor = mysql.connection.cursor()
        if request.method == 'POST' and 'booking' in request.form and 'type' in request.form and 'reason' in request.form:
                booking = request.form['booking']
                type = request.form['type']
                reason = request.form['reason']
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO form (booking, type, reason) VALUES (%s, %s, %s)''', (booking, type, reason))
                mysql.connection.commit()
                cursor.close()
        return render_template('home.html')


@app.route("/ENMNB", methods = ['GET', 'POST'])
def ENMNB():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT bookid FROM user WHERE email = % s', (session['email'], ))
        user = cursor.fetchall()
        bookings = [item[0] for item in user]
        return render_template('ENMNB.html', bookings = bookings)

@app.route("/BMMNB", methods = ['GET', 'POST'])
def BMMNB():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT bookid FROM user WHERE email = % s', (session['email'], ))
        user = cursor.fetchall()
        bookings = [item[0] for item in user]
        return render_template('BMMNB.html', bookings = bookings)

@app.route("/CNMNB", methods = ['GET', 'POST'])
def CNMNB():
    if session.get('loggedin') is None:
            return redirect('/',code=302)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT bookid FROM user WHERE email = % s', (session['email'], ))
        user = cursor.fetchall()
        bookings = [item[0] for item in user]
        return render_template('CNMNB.html', bookings = bookings)


@app.route('/', methods = ['GET', 'POST'])
def login():
    message = ''

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            
            return render_template('home.html', message = message)
        else:
            message = 'Incorrect email/password'
    
    return render_template('login.html', message = message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    session.pop('name', None)
    return redirect(url_for('login'))


@app.route("/chatEN", methods=['GET', 'POST'])
def svm_respond():   
    user_query = request.json
    # print(user_query)
    user_query = user_query['input']
    question = [user_query]
    if question[0] == "hi" or question[0] == "hello" or question[0] == "hey":
        result = random.choice(greet_response)
        return jsonify(result)

    elif question[0] == "bye" or question[0] == "goodbye"  :
        result = random.choice(bye_response)
        return jsonify(result)
        
        
    else:
   
        remove_punctuation(question[0])
        remove_stopwords(question[0])
        lemmatize_words(question[0])
        remove_urls(question[0])
        special_char(question[0])
        question[0].lower()
        question = vectsvm.transform(question)
        category = svm.predict(question)
        category = ",".join(str(x) for x in category)
        result = dict_from_csv[category]
        # print(result)
        return jsonify(result)
    # print(dict_from_csv[category])
    
@app.route("/chatBM", methods=['GET', 'POST'])
def svmBM_respond():   
    user_query = request.json
    # print(user_query)
    user_query = user_query['input']
    question = [user_query]
    if question[0] == "hai" or question[0] == "hi":
        result = random.choice(greet_BM)
        return jsonify(result)

    elif question[0] == "terima kasih" or question[0] == "jumpa lagi" :
        result = random.choice(bye_BM)
        return jsonify(result)
        
        
    else:
  
        remove_punctuation(question[0])
        remove_BMstopwords(question[0])
        BMlemmatizer(question[0])
        remove_urls(question[0])
        special_char(question[0])
        question[0].lower()
        question = vectsvmBM.transform(question)
        category = svmBM.predict(question)
        category = ",".join(str(x) for x in category)
        result = dict_from_csvBM[category]
        # print(result)
        return jsonify(result)

@app.route("/chatCN", methods=['GET', 'POST'])
def svmCN_respond():   
    user_query = request.json
    # print(user_query)
    user_query = user_query['input']
    question = [user_query]
    if question[0] == "你好":

        result = random.choice(greet_CN)
        return jsonify(result)

    elif question[0] == "谢谢" or question[0] == "再见" :
        result = random.choice(bye_CN)
        return jsonify(result)
        
        
    else:
 
        remove_punctuation(question[0])
        remove_CNstopwords(question[0])
        CNtokenizer(question[0])
        remove_urls(question[0])
        question = vectsvmCN.transform(question)
        category = svmCN.predict(question)
        category = ",".join(str(x) for x in category)
        result = dict_from_csvCN[category]
        # print(result)
        return jsonify(result)


@app.route("/chatMNBEN", methods=['GET', 'POST'])
def MNB_respond():   
    user_query = request.json
    # print(user_query)
    user_query = user_query['input']
    question = [user_query]
    if question[0] == "hi" or question[0] == "hello" or question[0] == "hey":
        result = random.choice(greet_response)
        return jsonify(result)

    elif question[0] == "bye" or question[0] == "goodbye" :
        result = random.choice(bye_response)
        return jsonify(result)
          
    else:
        remove_punctuation(question[0])
        remove_stopwords(question[0])
        lemmatize_words(question[0])
        remove_urls(question[0])
        special_char(question[0])
        question[0].lower()
        question = vectmnb.transform(question)
        category = mnb.predict(question)
        category = ",".join(str(x) for x in category)
        result = dict_from_csv[category]
        # print(result)
        return jsonify(result)
    # print(dict_from_csv[category])
    
@app.route("/chatMNBBM", methods=['GET', 'POST'])
def MNBBM_respond():   
    user_query = request.json
    # print(user_query)
    user_query = user_query['input']
    question = [user_query]
    if question[0] == "hai" or question[0] == "hi":
        result = random.choice(greet_BM)
        return jsonify(result)

    elif question[0] == "terima kasih" or question[0] == "jumpa lagi" :
        result = random.choice(bye_BM)
        return jsonify(result)
        
        
    else:
        remove_punctuation(question[0])
        remove_BMstopwords(question[0])
        BMlemmatizer(question[0])
        remove_urls(question[0])
        special_char(question[0])
        question[0].lower()
        question = vectmnbBM.transform(question)
        category = mnbBM.predict(question)
        category = ",".join(str(x) for x in category)
        result = dict_from_csvBM[category]
        # print(result)
        return jsonify(result)

@app.route("/chatMNBCN", methods=['GET', 'POST'])
def MNBCN_respond():   
    user_query = request.json
    # print(user_query)
    user_query = user_query['input']
    question = [user_query]
    if question[0] == "你好":
        result = random.choice(greet_CN)
        return jsonify(result)

    elif question[0] == "谢谢" or question[0] == "再见" :
        result = random.choice(bye_CN)
        return jsonify(result)
        
        
    else:
    
        remove_punctuation(question[0])
        remove_CNstopwords(question[0])
        CNtokenizer(question[0])
        remove_urls(question[0])
        question = vectmnbCN.transform(question)
        category = mnbCN.predict(question)
        category = ",".join(str(x) for x in category)
        result = dict_from_csvCN[category]
        # print(result)
        return jsonify(result)
























