import tweepy
import json

consumer_key = "SDCY9mKXQCQzEK9iNOGAFrOyK"
consumer_secret = "ZtEC5hDg1bqh9uLYPPCdUgtIynZ7zMjiHdOAcb7GA6C68sTJ1N"
access_token = "2739462773-ArMzguhFpdmsjKSL5Jde2RKlCT3iEIyEPiSzMM6"
access_token_secret = "YL2X9v1odmtpEfpG0F4xsOrTo1GO1NdCfVwbcf8mKdW3Q"


class StdOutListener(tweepy.Stream):
    """
    A listener handles tweets that are received from the stream.
    """

    def on_data(self, data):
        json_data = json.loads(data)
        tweets.append(json_data)
        tweets_file.write(str(data))

        user_location = json_data.get('user', {'location': None}).get('location')
        if 'amsterdam' in str(user_location).lower():
            # If location == amsterdam
            amsterdam_tweets_file.write(str(data))
            amsterdam_tweets.append(json_data)
            print('amsterdam', len(amsterdam_tweets), 'total', len(tweets))
            if any(substring in str(json_data.get('text')).lower() for substring in ['covid', 'corona', 'lockdown']):
                # If location == amsterdam && covid-related
                amsterdam_covid_tweets_file.write(str(data))
                amsterdam_covid_tweets.append(json_data)
                print('amsterdam covid', len(amsterdam_covid_tweets), 'total', len(tweets))

        if any(substring in str(json_data.get('text')).lower() for substring in ['covid', 'corona', 'lockdown']):
            # If covid-related
            covid_tweets_file.write(str(data))
            covid_tweets.append(json_data)
            print('covid', len(covid_tweets), 'total', len(tweets))

        return True

    def on_error(self, status):
        print(status)
        return True


tweets = []
amsterdam_tweets = []
covid_tweets = []
amsterdam_covid_tweets = []
tweets_file = open('../output/tweets.json', 'a')
amsterdam_tweets_file = open('../output/amsterdam_tweets.json', 'a')
covid_tweets_file = open('../output/covid_tweets.json', 'a')
amsterdam_covid_tweets_file = open('../output/amsterdam_covid_tweets.json', 'a')

stream = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
stream.sample()
# stream.filter(track=["python"])
