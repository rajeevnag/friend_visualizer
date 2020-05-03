
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

def get_mutual_connections(friends,friend_connections,choice):
    #friends is set containing usernames of people i'm following
    #friend_connections is dictionary mapping usernames of people i'm following to a set of our mutual friends

    import os.path
    from os import path
    import twint


    for friend in friends:

        if path.exists('direct_connections.txt'):#clear file 
                os.remove('direct_connections.txt')
        
        open('direct_connections.txt', 'w+').close()

        #get followers or people following user
        c = twint.Config()
        c.Username = friend
        c.Format = 'Name {name} Username {username}'
        c.Output = 'direct_connections.txt'

        if choice == 'following':
            twint.run.Following(c)
        else:
            twint.run.Followers(c)

        with open('direct_connections.txt','r+') as file:
            file.seek(0) #reset file position 
            connections = file.readlines()
            current_connections = set()
            for connection in connections:
                if connection in friends and connection not in current_connections:
                    current_connections.add(connection) 

            friend_connections[friend] = current_connections
            
            

        


    breakpoint()
    # for friend in friends:
    #     c = twint.Config()
    #     c.Username = friend
    #     c.Output = 'direct_connection.txt'

    
        
    #     if choice == 'following':
    #         twint.run.Following(c)
    #     else:
    #         twint.run.Followers(c)




def analyze_user(user_name):

    #data structures needed:
    # set containing usernames of friends (definitely needed)
    # dictionary mapping username to name  (probably needed)
    # dictionary mapping username to set of mutual friends



    #verify user exists
    user_name = get_real_username(user_name)

    print('Would you like to analyze who ' + user_name + ' is following or their followers?')

    choice = input()
    while choice != 'following' and choice != 'followers':
        print('invalid choice, pick again')
        choice = input()
    
    if choice == 'following':
        friends_info = Twitter.friends(user_name)
    else:
        friends_info = Twitter.followers(user_name)

    
    #dictionary for mapping username to name
    friends_username = dict()

    #first get set of all friends I have
    friends = set() #all of my friends (contains username, not actual name to avoid duplicate names)
    
    #assign set of friends and also dictionary mapping username to name
    for friend in friends_info:
        if friend.screen_name not in friends:
            friends.add(friend.screen_name)
            friends_username[friend.screen_name] = friend.name

    friend_connections = dict() #dictionary that stores username and all mutual friends

    get_mutual_connections(friends,friend_connections,choice)


        


import tweepy

consumer_key= 'FvflCo1aIlcLbeFfq9unJ9rli'
consumer_secret = 'MRMYvUFeTgVGCwktHfPvPt3EAseDIfMZfzCwrZ0tIvagC6hWat'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = '1244794411017535489-C2RFnu2E0yiJdEYVDlaEJBjR7mAkJm'
access_token_secret = 'yH9eeZtLkYjxcam2PGjpaQWw3g5sdSGjakarcIsto7nED'

auth.set_access_token(access_token, access_token_secret)

Twitter = tweepy.API(auth,wait_on_rate_limit=True)


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

