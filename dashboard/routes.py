
from dashboard import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
import praw, requests, json, sys, socket, random
from dashboard.models import User
from datetime import datetime
import numpy as np

from dashboard.models import  User
# from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from dashboard import db

scope_input = '*'
scopes = [scope.strip() for scope in scope_input.strip().split(",")]

reddit = praw.Reddit(
    client_id = 'tC-RStYYMyOXAVgtuVy3cA',
    client_secret = 'XIJwrc-zKpm-kMB7aR0MCE3DvDGpRw',
    redirect_uri="http://127.0.0.1:5000/auth",
    user_agent="obtain_refresh_token testing by u/Solid-Guidance1826 Im sorry, Im bad at this. contact:henryp959@gmail.com",
)
state = str(random.randint(0, 65000))

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return redirect(reddit.auth.url(scopes, state, "permanent"))

@app.route('/auth')
def auth():
    code = request.args.get('code')
    print('code:', code)
    print(reddit.auth.authorize(code))
    print(reddit.user.me())

    return redirect(url_for('dashboard_page'))


@app.route('/dashboard')
def dashboard_page():  
    jsdict = postingActivityDay()
    topSubs = topTenSubreddits()
    something = averageCommentLengths()
    return render_template('dashboard.html', jsdict=jsdict, topSubs = topSubs, something = something)
    

def postingActivityDay():
    supportSubs = ['test', 'videos','pcgaming']
    DoTW = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0,}
    comments =  reddit.user.me().comments.new(limit=50)
    for comment in comments:
        if(str(comment.subreddit) in supportSubs):
            unix_val = datetime.fromtimestamp(comment.created)
            day = unix_val.weekday()
            if(day == 0): day = 'Sunday'
            elif(day == 1): day = 'Monday'
            elif(day == 2): day = 'Tuesday'
            elif(day == 3): day = 'Wednesday'
            elif(day == 4): day = 'Thursday'
            elif(day == 5): day = 'Friday'
            elif(day == 6): day = 'Saturday'
            if(day in DoTW):
                DoTW[day] += 1
    return DoTW


def topTenSubreddits():
    subList = {}
    comments =  reddit.user.me().comments.new(limit=500)
    for comment in comments:
        if(str(comment.subreddit) in subList):
            subList[str(comment.subreddit)] += 1
        else:
            subList[str(comment.subreddit)] = 1
    topSubs = sorted(subList, key=subList.get, reverse=True)[:10]
    return subList
#I should probably change this to also compile a list of submissions
#also this all will probably need to be changed to pull this from a database
def averageCommentLengths():
    commentLengths = []
    supportSubs = ['test', 'videos','pcgaming']
    wordsMain = {}
    comments =  reddit.user.me().comments.new(limit=50)
    for comment in comments:
        if(str(comment.subreddit) in supportSubs):
            body = str(comment.body)
            wordList = body.split()
            for word in wordList:
                if word not in wordsMain:
                    wordsMain[word] = 1
                else:
                    wordsMain[word] += 1
            # if(len(body) > 5): to remove short replies from average
            commentLengths.append(len(body))

    # print(len(commentLengths))
    avg = np.average(commentLengths)
    median = np.median(commentLengths)
    # print("Average: " , avg)
    # print("Median: " , median)
    output = []
    output.append(avg) 
    output.append(median)
    output.append(commentLengths)
    output.append(wordsMain)
    return output




