from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from blog_project.utils import success_resp, error_resp, get_value_or_404,send_mail, get_value_or_default
from .serializers import PostSerializer
from posts.models import Post
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
# from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.


@api_view(["POST","GET"])
def enter_detail(request):
    '''
    Post Api is used to create data in a database
    Get Api view is for viewing data of database
    '''
    tutorial_serializer = PostSerializer()
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        tutorial_serializer = PostSerializer(data=data)
        if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif(request.method == 'GET'):
        obj = Post.objects.all()
        l=[]
        for i in obj:
            serializer = PostSerializer(i).data
            l.append(serializer)
        return Response(success_resp(l))

    else:
        pass


@api_view(["PUT","GET"])
def update_detail(request,pk):
    '''
    This Api is used to edit detail of given detail.
    '''
    try:
        obj = Post.get_detail(pk)
    except Exception as E:
        return Response("user doesnot exist")
    if (request.method == "PUT"):
        data = JSONParser().parse(request)
        tutorial_serializer = PostSerializer(obj,data=data)
        if tutorial_serializer.is_valid(): 
                tutorial_serializer.save() 
                return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif (request.method == "GET"):
        tutorial_serializer = PostSerializer(obj) 
        return Response(tutorial_serializer.data) 
    
    else:
        pass







