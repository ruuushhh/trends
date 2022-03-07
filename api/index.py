import tweepy
import pandas as pd
from GoogleNews import GoogleNews
from transformers import pipeline
from fastapi.responses import StreamingResponse
import uuid
import io

consumer_key = "qrKLlj03Ka5ZUuwXTS6El72VY"
consumer_secret = "CLhbypeKTFD4kb7B5qMLXUuKevTWXqPjdZx46DD4rNrZHiTWVC"
access_token = "3129860960-L1HNhp6KxgMIRL8CIF1btEfDafUhcRXz2PNP4Ye"
access_token_secret = "7RvoqlZt6JEAAxD4fpRYNwui9T3tzRZBQGafXuiiLYrnv"

sentiment_analysis = pipeline("sentiment-analysis")

columns = ["Date", "Content", "Source", "Sentiment"]
data = []


def twitter_data():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    cursor = tweepy.Cursor(
        api.search_tweets, q="Green Hydrogen", tweet_mode="extended"
    ).pages(120)
    return cursor


def google_news_data():
    news = GoogleNews("en", "d")
    news.set_time_range("02/01/2022", "03/01/2022")
    news.set_encode("utf-8")
    news.search("Green Hydrogen")
    news_data = news.result()
    return news_data


def all_data_to_csv():
    twitter = twitter_data()
    google = google_news_data()
    for news in google:
        sentiment = sentiment_analysis(news["desc"])
        data.append([news["date"], news["desc"], news["link"], sentiment[0]["score"]])
    for tweets in twitter:
        for tweet in tweets:
            sentiment = sentiment_analysis(tweet.full_text)
            data.append(
                [
                    tweet.created_at,
                    tweet.full_text,
                    tweet.user.screen_name,
                    sentiment[0]["score"],
                ]
            )

    df = pd.DataFrame(data, columns=columns)
    unique_filename = str(uuid.uuid4())
    df.to_csv(("csv_files\\" + unique_filename + ".csv"), index=False)
    response = StreamingResponse(
        io.StringIO(df.to_csv(index=False)), media_type="text/csv"
    )
    return response
