from rest_framework import serializers
from article.models import Article
from datetime import datetime


class ArticleSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(required=True,max_length=100)
    category = serializers.CharField(max_length=50)
    date_time = serializers.DateTimeField(default=datetime.now())
    content = serializers.CharField()


    def create(self, validated_data):
        return Article.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title= validated_data.get('title',instance.title)
        instance.category= validated_data.get('category',instance.category)
        instance.date_time = validated_data.get('date_time',instance.date_time)
        instance.content = validated_data.get('content',validated_data.content)
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = ('id','title','category','date_time','content')

