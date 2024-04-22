import requests
from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from model.tweet_model import tweet_model
from datetime import datetime
obj = tweet_model()


blp = Blueprint("tweets", __name__, description="Operations on tweets resource")

@blp.route("/api/v1/tweets")
class GetAllTweets(MethodView):

    def get(self):
        try:
            return jsonify(obj.all_tweets()), 200
        except KeyError:
            abort(404, message="Tweet Not Found.")

@blp.route("/api/v1/trending_hashtags")
class GetTopHashtags(MethodView):

    def get(self):
        try:
            time_stamp_str = request.args.get('time_stamp')
            time_stamp = datetime.fromisoformat(time_stamp_str)
            return jsonify(obj.most_trending_hashtags(time_stamp)),200
        except KeyError:
            abort(404, message="No Hashtags Found.")

@blp.route("/api/v1/tweets/tweet_text")
class FindTweetsByKeyWord(MethodView):

    def get(self):
        try:
            key_word = request.args.get('tweet_text')
            lang = request.args.get('lang')
            return jsonify(obj.query_tweets_by_keyword(key_word,lang)), 200
        except KeyError:
            abort(404, message="Tweet Not Found.")
