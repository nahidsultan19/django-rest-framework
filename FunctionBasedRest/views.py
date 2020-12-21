# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BookRest
from .serializers import BookRestSerializer

# module for authentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def ApiView(request):
    api_list = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Detail': '/detail/<str:pk>/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_list)


# list and create item
@api_view(['GET', 'POST'])
def List(request):
    if request.method == 'GET':
        book = BookRest.objects.all()
        serializer = BookRestSerializer(book, many=True)
        return Response(serializer.data)
    else:
        serializer = BookRestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# Update, Detaile and Delete


@api_view(['GET', 'POST', 'DELETE'])
def Update(request, pk):
    if request.method == 'POST':
        book = BookRest.objects.get(id=pk)
        serializer = BookRestSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        book = BookRest.objects.get(id=pk)
        serializer = BookRestSerializer(book, many=False)
        return Response(serializer.data)
    else:
        book = BookRest.objects.get(id=pk)
        book.delete()
        return Response('Item successfully deleted!')
