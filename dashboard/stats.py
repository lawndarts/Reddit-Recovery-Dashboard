
from datetime import datetime
import numpy as np
# import nltk

subsDict = {}
with open('dashboard/subreddits.txt') as myfile:
    for line in myfile:
        name, description = line.partition("=")[::2]
        subsDict[name.strip()] = description.strip()
supportSubs = list(subsDict.keys())
for i in range(len(supportSubs)):
    supportSubs[i] = supportSubs[i][2:]

def getAccountAge(user):
    date = datetime.fromtimestamp(user.created_utc)
    now = datetime.now()
    difference = now - date
    years = difference.days / 365
    # days = difference % 365

    return difference.days

def postingActivityDay(comments):
    supportSubs = ['test', 'videos','pcgaming']
    DoTW = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0,}
    for comment in comments:
        # if(str(comment.subreddit) in supportSubs):
            unix_val = datetime.fromtimestamp(comment['created'])
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

# returns two dictionaries in a list. One contains submission frequency,
# the other has comment frequency both sorted by subreddit
def activityCountSubreddit(comments, submissions):
    subListComments = {}
    subListSubmissions = {}
    for comment in comments:
        if(str(comment['subreddit']) in subListComments):
            subListComments[str(comment['subreddit'])] += 1
        else:
            subListComments[str(comment['subreddit'])] = 1
    for submission in submissions:
        if(str(submission['subreddit']) in subListSubmissions):
            subListSubmissions[str(submission['subreddit'])] += 1
        else:
            subListSubmissions[str(submission['subreddit'])] = 1
    aList = []
    aList.append(subListComments)
    aList.append(subListSubmissions)
    return aList

def getMax(theDict):
    max_key = max(theDict, key=theDict.get)
    return max_key

def wordsDict(comments):
    supportSubs = ['test', 'videos','pcgaming']
    wordsMain = {}
    for comment in comments:
        # if(str(comment.subreddit) in supportSubs):
            body = str(comment['body'])
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
        # if(str(comment.subreddit) in supportSubs):
            body = str(comment['body'])
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
    
    return subsDict

def commentsOnDaysEngaged(comments):
    stats = []
    supportSubs = ['test', 'videos', 'pcgaming']
    commentDates = {}
    totalComments = 0
    for comment in comments:
        # if(str(comment['subreddit']) in supportSubs):
            
            unix_val = datetime.fromtimestamp(comment['created'])
            strippedDate = unix_val.date()
            if(strippedDate in commentDates):
                commentDates[strippedDate] += 1
                totalComments += 1
            else:
                commentDates[strippedDate] = 1
                totalComments += 1
    res = sum(commentDates.values()) / totalComments
    # stats.append(res)
    return res

# def sentimentAnalysis(upvotes):
#     high = []
#     low = []
#     nltk.download('vader_lexicon')
#     # Initialize the VADER sentiment analyzer
#     from nltk.sentiment.vader import SentimentIntensityAnalyzer
#     analyzer = SentimentIntensityAnalyzer()
    # result = {}
    # commentList = []
    # comments =  reddit.user.me().comments.new(limit=50)
    # #generate list of comments
    # for comment in comments:
    #     if(str(comment.subreddit) in subreddit):
    #         if(len(comment.body)) > 10:
    #             commentList.append(str(comment.body))

    #get sentiment analysis per subreddit

    # result = {'pos': 0, 'neg': 0, 'neu': 0}
    # for comment in commentList:
    #     score = analyzer.polarity_scores(comment)
    #     if score['compound'] > 0.05:
    #         result['pos'] += 1
    #     elif score['compound'] < -0.05:
    #         result['neg'] += 1
    #     else:
    #         result['neu'] += 1

    # print(result)       
    # return 0

#should accept all three dictionaries with their respective frequencies organized by subreddit
def getMaxValues(comments, submissions, upvotes):
    
    return 0

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

def getUpvotedSubreddits(user):
    global sortedSubDict
    #get posts upvoted by user
    #user = reddit.redditor('kah277')
    upvotedPosts = user.upvoted()

    #put subreddit name and upvote totals in dictionary
    subredditDict = {}

    for u in upvotedPosts:

        if u.subreddit.display_name not in subredditDict:
            subredditDict[u.subreddit.display_name] = 1
        else:
            subredditDict[u.subreddit.display_name]+=1

    #sort it from highest count to lowest
    sortedSubDict = dict(sorted(subredditDict.items(), key=lambda x: x[1], reverse=True))
    return sortedSubDict
def getPostSubreddits(user):
    global subredditPostDictionary 
    #get posts upvoted by user
    #user = reddit.redditor('kah277')
    posts = user.submissions.new(limit=None)

    #put subreddit name and upvote totals in dictionary
    subredditPostDict = {}

    for p in posts:
        if p.subreddit.display_name not in subredditPostDict:
            subredditPostDict[p.subreddit.display_name]=1
        else:
            subredditPostDict[p.subreddit.display_name]+=1

    #sort it from highest count to lowest
    subredditPostDictionary  = dict(sorted(subredditPostDict.items(), key=lambda x: x[1], reverse=True))
    return subredditPostDictionary 
def getCommentSubreddits(user):
    global subredditCommentDictionary
    #get posts upvoted by user
    #user = reddit.redditor('kah277')
    comments = user.comments.new(limit=None)

    #put subreddit name and upvote totals in dictionary
    subredditCommentDict = {}

    for c in comments:
        if c.subreddit.display_name not in subredditCommentDict:
            subredditCommentDict[c.subreddit.display_name]=1
        else:
            subredditCommentDict[c.subreddit.display_name]+=1

    #sort it from highest count to lowest
    subredditCommentDictionary = dict(sorted(subredditCommentDict.items(), key=lambda x: x[1], reverse=True))
    return subredditCommentDictionary
