
def get_real_username(user_name):
    search_result = list()
    search_result = Twitter.search_users(user_name)
    
    while Twitter.search_users(user_name) == list():
        print('Invalid user, pick again')
        user_name = input()
    
    idx = 1
    print('results:')
    for person in search_result:
        
        print(str(idx) +': ' + person.screen_name)
        idx += 1
    
    if idx > 2:# if more than 1 search result
        print('Which person do you want?')
        choice = int(input())
    else:
        choice = 1
    while choice-1 < 0 and choice-1 > len(search_result):
        print('Invalid choice number, pick again')
        choice = input()

    
    user_name = search_result[choice-1].screen_name
    return user_name

def analyze_user(user_name):
    #verify user exists
    user_name = get_real_username(user_name)
    friends = Twitter.friends(user_name)
    for friend in friends:
        print(friend.name)
        
    breakpoint()
    x = 4


import tweepy

consumer_key= 'FvflCo1aIlcLbeFfq9unJ9rli'
consumer_secret = 'MRMYvUFeTgVGCwktHfPvPt3EAseDIfMZfzCwrZ0tIvagC6hWat'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = '1244794411017535489-C2RFnu2E0yiJdEYVDlaEJBjR7mAkJm'
access_token_secret = 'yH9eeZtLkYjxcam2PGjpaQWw3g5sdSGjakarcIsto7nED'

auth.set_access_token(access_token, access_token_secret)

Twitter = tweepy.API(auth)


while True:
    print("Input username you'd like to analyze")
    user_name = input()
    analyze_user(user_name)
    print("Would you like to analyze another user? (y/n)")
    answer = input()
    while answer != 'y' and answer != 'n':
        print("invalid answer... try again")
        answer = input()
    if answer == 'n':
        break

