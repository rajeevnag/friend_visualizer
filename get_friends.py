
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

def get_mutual_connections(friends,friend_connections):
    #friends is set containing usernames of people i'm following
    #friend_connections is dictionary mapping usernames of people i'm following to a set of our mutual friends
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import sys

    driver = webdriver.Chrome(ChromeDriverManager().install())

    #login to twitter first
    
    login_url = 'https://twitter.com/login' 
    driver.get(login_url)

    breakpoint()
    username_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'
    password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'
    login_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div'

    username_button = driver.find_element_by_xpath(username_xpath)
    password_button = driver.find_element_by_xpath(password_xpath)
    login_button = driver.find_element_by_xpath(login_button_xpath)

    print('input username to log in to twitter')
    real_username = input()

    print('input password to log in to twitter')
    real_password = input()

    
    username_button.send_keys(real_username)
    time.sleep(1)
    password_button.send_keys(real_password)
    time.sleep(2)

    login_button.click()



    try:
        for friend in friends:
            
            #url for user search results
            url = 'https://twitter.com/{username}/following'.format(username=friend)
            driver.get(url)
            time.sleep(1) #sleep for 1 second to allow page to load
            breakpoint()
            try:
                breakpoint()

            except:
                print('Error: ')
                print(sys.exc_info()[0])
                print()
                breakpoint()

            print('hi')
            print(friend)
            breakpoint()

        driver.close()
    except:
        driver.close()
        print('error')


def analyze_user(user_name):

    #data structures needed:
    # set containing usernames of friends (definitely needed)
    # dictionary mapping username to name  (probably needed)
    # dictionary mapping username to set of mutual friends



    #verify user exists
    user_name = get_real_username(user_name)
    friends_info = Twitter.friends(user_name)
    
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

    get_mutual_connections(friends,friend_connections)


        


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

