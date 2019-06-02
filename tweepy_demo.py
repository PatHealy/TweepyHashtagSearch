import tweepy
from tweepy import Status

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

with open('tweepy_config') as config_file:
    consumer_key = config_file.readline().strip()
    consumer_secret = config_file.readline().strip()
    access_token = config_file.readline().strip()
    access_token_secret = config_file.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = tweepy.Cursor(api.search, q="#SpellingBee", tweet_mode='extended').items(20)
for tweet in public_tweets:
    print("id: " + str(tweet.id))
    print("author: " + str(tweet.author.name) + ", @" + str(tweet.author.screen_name))
    print('retweeted_status: ' + str('retweeted_status' in vars(tweet).keys()))
    print("text: " + str(tweet.full_text))
    if 'extended_entities' in tweet._json and 'media' in tweet._json['extended_entities']:
        out = 'extended media: '
        #print(tweet._json['extended_entities'])
        for m in tweet._json['extended_entities']['media']:
            out = out + str(m['media_url']) + ', '
        out = out[:-2]
        print(out)
    elif 'media' in tweet.entities:
        out = 'media: '
        #print(tweet.entities)
        for m in tweet.entities['media']:
            out = out + str(m['media_url']) + ', '
        out = out[:-2]
        print(out)
    print()


# Attributes of a Status object
#_api
#_json
#created_at
#id
#id_str
#text
#truncated
#entities
#source
#source_url
#in_reply_to_status_id
#in_reply_to_status_id_str
#in_reply_to_user_id
#in_reply_to_user_id_str
#in_reply_to_screen_name
#author
#user
#geo
#coordinates
#place
#contributors
#retweeted_status
#is_quote_status
#quoted_status_id
#quoted_status_id_str
#retweet_count
#favorite_count
#favorited
#retweeted
#possibly_sensitive
#possibly_sensitive_appealable
#lang



#Attributes of User objects
#_api
#_json
#id
#id_str
#name
#screen_name
#location
#description
#url
#entities
#protected
#followers_count
#friends_count
#listed_count
#created_at
#favourites_count
#utc_offset
#time_zone
#geo_enabled
#verified
#statuses_count
#lang
#contributors_enabled
#is_translator
#is_translation_enabled
#profile_background_color
#profile_background_image_url
#profile_background_image_url_https
#profile_background_tile
#profile_image_url
#profile_image_url_https
#profile_banner_url
#profile_link_color
#profile_sidebar_border_color
#profile_sidebar_fill_color
#profile_text_color
#profile_use_background_image
#has_extended_profile
#default_profile
#default_profile_image
#following
#follow_request_sent
#notifications
#translator_type