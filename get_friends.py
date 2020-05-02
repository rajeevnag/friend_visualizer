
import tweepy

consumer_key= 'FvflCo1aIlcLbeFfq9unJ9rli'
consumer_secret = 'MRMYvUFeTgVGCwktHfPvPt3EAseDIfMZfzCwrZ0tIvagC6hWat'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = '1244794411017535489-C2RFnu2E0yiJdEYVDlaEJBjR7mAkJm'
access_token_secret = 'yH9eeZtLkYjxcam2PGjpaQWw3g5sdSGjakarcIsto7nED'

auth.set_access_token(access_token, access_token_secret)

Twitter = tweepy.API(auth)

search_result = Twitter.search_users('jeevs')
breakpoint()
print('hi')

