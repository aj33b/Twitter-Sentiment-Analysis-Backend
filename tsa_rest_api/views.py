from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from tsa_rest_api.models import ClassifiedTweets
from tsa_rest_api.serializers import ClassifiedTweetsSerializer


# Create your views here.

@csrf_exempt
def index(request, id=0):
    # Show individual data or specific data.
    if request.method == 'GET':
        try:
            id
        except NameError:
            classified_tweets = ClassifiedTweets.objects.all()
            classified_tweets_serializer = ClassifiedTweetsSerializer(classified_tweets, many=True)
            return JsonResponse(classified_tweets_serializer.data, safe=False)
        else:
            classified_tweets = ClassifiedTweets.objects.get(id=id)
            classified_tweets_serializer = ClassifiedTweetsSerializer(classified_tweets, many=False)
            return JsonResponse(classified_tweets_serializer.data, safe=False)

    # Add new data.
    elif request.method == 'POST':
        classified_tweets_data = JSONParser().parse(request)
        classified_tweets_serializer = ClassifiedTweetsSerializer(data=classified_tweets_data)
        if classified_tweets_serializer.is_valid():
            classified_tweets_serializer.save()
            return JsonResponse("Data added successfully", safe=False)
        return JsonResponse("Failed to add new data", safe=False)

    # Update existing data.
    elif request.method == 'PUT':
        classified_tweets_data = JSONParser().parse(request)
        classified_tweet = ClassifiedTweets.objects.get(id=id)
        classified_tweets_serializer = ClassifiedTweetsSerializer(classified_tweet, data=classified_tweets_data)
        if classified_tweets_serializer.is_valid():
            classified_tweets_serializer.save()
            return JsonResponse("Data updated successfully", safe=False)
        return JsonResponse("Failed to update data", safe=False)

    # Delete existing data.
    elif request.method == 'DELETE':
        classified_tweet = ClassifiedTweets.objects.get(id=id)
        classified_tweet.delete()
        return JsonResponse("Data deleted successfully", safe=False)
