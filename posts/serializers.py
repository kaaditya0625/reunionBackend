from .models import Post, Like, Followers, Comment
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def delete(self):
        instance = self.instance
        instance.delete()

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = '__all__'

    def validate(self,data):
        if data['follower'] == data['following']:
            raise serializers.ValidationError('You can not follow yourself')
        return data

    def delete(self):
        instance = self.instance
        instance.delete()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    no_likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'  

    def get_no_likes(self, obj):
        return obj.likes.count()          