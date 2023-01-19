import tweepy
import json

consumer_key = "Insert your own key here"
consumer_secret = "Insert your own key here"
access_token = "Insert your own key here"
access_token_secret = "Insert your own key here"
bearer_token = "Insert your own key here"


class Listener(tweepy.Stream):
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


if __name__ == '__main__':
    tweets = []
    amsterdam_tweets = []
    covid_tweets = []
    amsterdam_covid_tweets = []

    tweets_file = open('output/tweets.json', 'a')
    amsterdam_tweets_file = open('output/amsterdam_tweets.json', 'a')
    covid_tweets_file = open('output/covid_tweets.json', 'a')
    amsterdam_covid_tweets_file = open('output/amsterdam_covid_tweets.json', 'a')

    # If you get the Too Much Requests error message, wait 10 minutes.
    stream = Listener(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.filter(track=["Twitter"])
