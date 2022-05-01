from rest_framework import serializers
from tsa_rest_api.models import ClassifiedTweets


class ClassifiedTweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifiedTweets
        fields = ('tweet', 'sentiment')
