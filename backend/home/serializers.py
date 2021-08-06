from rest_framework import serializers
from .models import Post
from .models import Author

#specifies the model to work with and the fields to be converted to JSON.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'category', 'content', 'author', 'create_date')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'netid')