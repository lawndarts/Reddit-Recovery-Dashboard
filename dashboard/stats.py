
from datetime import datetime
import numpy as np

def postingActivityDay(comments):
    supportSubs = ['test', 'videos','pcgaming']
    DoTW = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0,}
    # comments =  reddit.user.me().comments.new(limit=50)
    for comment in comments:
        # if(str(comment.subreddit) in supportSubs):
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


def topTenSubreddits(comments):
    subList = {}
    # comments =  reddit.user.me().comments.new(limit=500)
    for comment in comments:
        if(str(comment.subreddit) in subList):
            subList[str(comment.subreddit)] += 1
        else:
            subList[str(comment.subreddit)] = 1
            
    # topSubs = sorted(subList, key=subList.get, reverse=True)[:10]
    print(subList)
    return subList
#I should probably change this to also compile a list of submissions
#also this all will probably need to be changed to pull this from a database
def random(comments):
    print('something')

def wordsDict(comments):
    supportSubs = ['test', 'videos','pcgaming']
    wordsMain = {}
    for comment in comments:
        if(str(comment.subreddit) in supportSubs):
            body = str(comment.body)
            wordList = body.split()
            for word in wordList:
                if word not in wordsMain:
                    wordsMain[word] = 1
                else:
                    wordsMain[word] += 1
    return wordsMain

def averageCommentLengthSupport(comments):
    commentLengths = []
    supportSubs = ['test', 'videos','pcgaming']
    for comment in comments:
        if(str(comment.subreddit) in supportSubs):
            body = str(comment.body)
            if(len(body) > 5): #dont count comments less than 5 characters
                commentLengths.append(len(body))

    avg = np.average(commentLengths)
    median = np.median(commentLengths)
    limited_float = round(avg, 2)
    output = []
    output.append(limited_float) 
    output.append(median)
    return output

def getSupportSubs():
    subsDict = {}
    with open('dashboard\subreddits.txt') as myfile:
        for line in myfile:
            name, description = line.partition("=")[::2]
            subsDict[name.strip()] = description.strip()
    print(subsDict)
    return subsDict

def get_subreddit_stats(subreddit):
    '''
    Get stats for a subreddit.

    Keyword arguments:
    subreddit = an instance of Praw's subreddit class. 

    Returns a dictionary.
    
    '''
    sub_stats = {
        'title': subreddit.display_name,
        'description': subreddit.public_description,
        'subscriber_count': subreddit.subscribers
    }
    return sub_stats

def get_post_history(user):
    '''
    Get user's post history.

    Keyword arguments:
    user = an instance of Praw's redditor class.

    Returns a list of each post (as a dictionary).
    
    '''
    post_history = []
    for submission in user.submissions.new():
        temp = submission.subreddit
        post = {
            'id': submission.id,
            'title': submission.title,
            'created': submission.created_utc,
            'subreddit': temp.display_name,
            'body':submission.selftext,
            'num_comments': submission.num_comments
        } 
        post_history.append(post)
    return post_history

def get_posts_in_subreddit(post_history, subreddit):
    '''
    Get user's posts in subreddit.

    Keyword arguments:
    post_history = list returned from get_post_history(user).
    subreddit = instance of Praw's subreddit class.

    Returns a list of : [title (str), date created (str), parent subreddit (Subreddit class), body text (str), number of comments (int) ]
    '''
    posts_in_subreddit = []
    for post in post_history:
        if post['subreddit'] == subreddit:
            posts_in_subreddit.append(post)
    return posts_in_subreddit

def get_comment_history(user):
    '''
    Get user's comment history.

    Keyword arguments:
    user = an instance of Praw's redditor class.

    Returns a list: [date created, comment id (str), parent subreddit (Subreddit class), body text (str)]
    
    '''
    comment_history = []
    for comment in user.comments.new():
        temp = comment.subreddit
        x = {
            'id': comment.id,
            'created': comment.created_utc,
            'post': comment.submission.id,
            'subreddit': temp.display_name,
            'body': comment.body
        }
        comment_history.append(x)
    return comment_history

def get_comments_in_subreddit(comment_history, subreddit):
    '''
    Get user's comments in a subreddit.

    Keyword arguments:
    comment_history = list returned from get_comment_history(user).
    subreddit = instance of Praw's subreddit class.

    Returns a list: [date created, comment id (str), parent subreddit (Subreddit class), body text (str)]
    '''
    comments_in_subreddit = []
    for comment in comment_history:
        if comment["subreddit"] == subreddit.display_name:
            comments_in_subreddit.append(comment)
    return comments_in_subreddit