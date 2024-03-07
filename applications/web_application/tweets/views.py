from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet, User, SearchTerm
from .serializers import TweetSerializer, UserSerializer, SearchTermSerializer
from rest_framework.response import Response

def index(request):
    list = Tweet.objects.all()
    str = ''
    for tweet in list:
        str.append(tweet.associated_user.username + ": " + tweet.text + "\n")
    return HttpResponse(str)

from rest_framework import viewsets, status

class TweetViewSet(viewsets.ViewSet):
    def list(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = TweetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        tweet = Tweet.objects.get(id=pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def update(self,request,pk=None):
        tweet = Tweet.objects.get(id=pk)
        serializer = TweetSerializer(instance=tweet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        tweet = Tweet.objects.get(id=pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self,request,pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SearchTermViewSet(viewsets.ViewSet):
    def list(self, request):
        terms = SearchTerm.objects.all()
        serializer = SearchTermSerializer(terms, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = SearchTermSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        term = SearchTerm.objects.get(id=pk)
        serializer = SearchTermSerializer(term)
        return Response(serializer.data)

    def update(self,request,pk=None):
        term = SearchTerm.objects.get(id=pk)
        serializer = SearchTermSerializer(instance=term, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        term = SearchTerm.objects.get(id=pk)
        term.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)