import praw as praw
import urllib.request
import json

with open('credidentials.json', 'r') as f:
    creds = json.load(f)

reddit = praw.Reddit(
    client_id=creds['client_id'],
    client_secret=creds['client_secret'],
    user_agent=creds['user_agent'],
    username=creds['username'],
)


def downloadFromTop(sub):
    count = 0
    for submission in subreddit.top(limit=None):
        url = str(submission.url)

        if url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png'):
            urllib.request.urlretrieve(url, f'image{count}')
            count += 1

            if count == 10:
                break


def downloadFromHot(sub):
    count = 0
    for submission in subreddit.hot(limit=None):
        url = str(submission.url)

        if url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png'):
            urllib.request.urlretrieve(url, f'image{count}')
            count += 1

            if count == 10:
                break


def downloadFromNew(sub):
    count = 0
    for submission in subreddit.new(limit=None):
        url = str(submission.url)

        if url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png'):
            urllib.request.urlretrieve(url, f'image{count}')
            count += 1

            if count == 10:
                break



print('Please choose only one at a time option')
print('1.Download from top')
print('2.Download from hot')
print('3.Download from new')
option = int(input('Your option: '))

if option == 1:
    print('You choose to download from top')
    sub_name = input('Enter subreddit\'s name: ')
    subreddit = reddit.subreddit(sub_name)
    downloadFromTop(sub_name)
elif option == 2:
    print('You choose to download from hot')
    sub_name = input('Enter subreddit\'s name: ')
    subreddit = reddit.subreddit(sub_name)
    downloadFromHot(sub_name)
elif option == 3:
    print('You choose to download from new')
    sub_name = input('Enter subreddit\'s name: ')
    subreddit = reddit.subreddit(sub_name)
    downloadFromNew(sub_name)
else:
    print('Invalid option')
