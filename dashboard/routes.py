#Need flask/flask_login packages below, flask-sqlalchemy, and psychopg2 installed in working python environment

from dashboard import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
import praw, random
from dashboard.models import User
# Import dashboard python functions
from dashboard import stats

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
    uname = str(reddit.user.me())
    user = User.query.filter_by(username=uname).first()
    if user:
        login_user(user)
        flash(f"Welcome back. You are logged in as {user.username}", category='success')
        print(f"Welcome back. You are logged in as {user.username}")
    else:
        user = User(username=uname)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f"Account successfully created. You are logged in as {user.username}", category='success')
        print(f"Account successfully created. You are logged in as {user.username}")
    return redirect(url_for('dashboard_page'))

@app.route('/support_subs')
def show_support_subs():
    subsDict = stats.getSupportSubs()
    return render_template('support_subs.html', subsDict = subsDict)

@app.route('/dashboard')
@login_required
def dashboard_page():
    #why do I need to make the comments object multiple times? 
    # if type(comments) == 'NoneType':
    #     return render_template(url_for('error_page'))

    # Henry's code
    comments =  reddit.user.me().comments.new(limit=50)
    jsdict = stats.postingActivityDay(comments)
    comments =  reddit.user.me().comments.new(limit=500)
    submissions = reddit.user.me().submissions.new()
    topSubs = stats.activityCountSubreddit(comments, submissions)
    comments =  reddit.user.me().comments.new(limit=50)
    avgStats = stats.averageCommentLengthSupport(comments)
    comments =  reddit.user.me().comments.new(limit=50)
    mainSupportSub = stats.getMainSupportSub(topSubs)
    


    sortedSubDict = stats.getUpvotedSubreddits(reddit.user.me())
    li = list(sortedSubDict.keys())
    upvoteCounts = list(sortedSubDict.values())      
    return render_template('dashboard.html',jsdict=jsdict,topSubs=topSubs,avgStats=avgStats,
            li=li,upvoteCounts=upvoteCounts,mainSupportSub=mainSupportSub)

@app.route('/subreddit/<name>')
def subreddit(name):
    #replace with database query
    post_history = stats.get_post_history(reddit.user.me())
    comment_history = stats.get_comment_history(reddit.user.me())
    posts_in_sub = stats.get_posts_in_subreddit(post_history, reddit.subreddit(name))
    post_count = len(posts_in_sub)
    comments_in_sub = stats.get_comments_in_subreddit(comment_history, reddit.subreddit(name))
    comment_count = len(comments_in_sub)
    sub_stats = stats.get_subreddit_stats(reddit.subreddit(name))
    title = sub_stats['title']
    description = sub_stats['description']
    subscriber_count = sub_stats['subscriber_count']  
    
    return render_template("subreddit.html", title = title, description = description, subscriber_count = subscriber_count, post_count = post_count, comment_count = comment_count)

    
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home_page'))





