import tweepy
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.

@csrf_exempt
def index(request):
    if request.GET.get('search', None) == "":
        return JsonResponse({"message": "Cannot fetch tweets for empty search"},
                            status=400,
                            safe=False)
    search = request.GET.get('search', None) + " -is:retweet" + " lang:en"
    if request.method == 'GET':
        tweepy_client = tweepy.Client(bearer_token=settings.TWITTER_BEARER_TOKEN)
        recent_tweets = (
            tweepy_client.search_recent_tweets(query=search, max_results=10, expansions=['author_id'],
                                               tweet_fields=['created_at', 'lang']))
        # users = {u['id']: u for u in recent_tweets.includes['users']}
        data = []
        for tweet in recent_tweets.data:
            # user = users[tweet.data.author_id]
            data.append(tweet.data)
        return JsonResponse(
            {"message": "Fetch Tweets API called successfully", "data": data},
            status=200,
            safe=False)
