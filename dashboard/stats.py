
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