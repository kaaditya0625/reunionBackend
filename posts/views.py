from rest_framework import generics
from .serializers import *
from .models import Post, Like, Followers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
# login_required


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.pk)

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = LikeSerializer(data={"user":request.user.pk,"post":kwargs.get("id")})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        likeInstance = Like.objects.filter(user=request.user.pk, post=kwargs["id"])
        if likeInstance:
            serializer = LikeSerializer(instance = likeInstance)
            serializer.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LikeListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     id = self.kwargs.get('id')
    #     # Filter the queryset based on the `id` parameter
    #     queryset = Like.objects.filter(post_id=id)
    #     return queryset

class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get(self, request, *args, **kwargs):
    #     # print(request.user.pk)
    #     comments = Comment.objects.filter(post_id=kwargs.get("id"))
    #     serializer = self.get_serializer(data={"comments":comments})
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
    #         print(serializer.errors)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def post(self, request, *args, **kwargs):
        # print(request.user.pk)
        serializer = self.get_serializer(data={"comment":request.data["comment"]})
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class CommentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.kwargs.get('id')
        # Filter the queryset based on the `id` parameter
        queryset = Comment.objects.filter(post_id=id)
        return queryset 

class FollowersCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer

class FollowersCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Followers.objects.all()
    # serializer_class = FollowersSerializer

    def post(self, request, *args, **kwargs):
        # print(request.user)
        print(kwargs)
        serializer = FollowersSerializer(data={"follower":request.user.pk,"following":kwargs.get("id")})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            # headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowersDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer

    def post(self, request, *args, **kwargs):
        print(kwargs)
        print(request.data)
        followInstance = self.get_queryset().filter(follower=request.user.id, following=kwargs["id"])

        if followInstance:
            serializer = self.get_serializer(instance = followInstance)
            serializer.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        result = {}
        result["name"] = request.user.username
        result['followers'] = Followers.objects.filter(following=request.user.pk).count()
        result['following'] = Followers.objects.filter(follower=request.user.pk).count()

        return Response(result)

        