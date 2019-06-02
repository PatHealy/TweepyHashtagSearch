# TweepyHashtagSearch
A simply python script using Tweepy that generates a spreadsheet of tweets that have used a given hashtag.

## Usage
```
python hashtag_search.py <hashtag> <output_file_name> [<limit>]
    -hashtag: the hashtag you're searching for
    -output_file_name: the name of the file this will be saved to (will be extended with .csv)
    -limit: the maximum number of tweets you want to query (optional)
```
This application also requires a configuration file named 'tweepy_config' with four lines of text representing the consumer_key, consumer_secret, access_token, and access_token_secret, respectively. For details, consult [the tweepy documentation.](https://tweepy.readthedocs.io/en/latest/auth_tutorial.html)