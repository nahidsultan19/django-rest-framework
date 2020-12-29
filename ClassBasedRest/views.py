# from django.shortcuts import render

# # Create your views here.

# from FunctionBasedRest.models import BookRest
# from FunctionBasedRest.serializers import BookRestSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response

# from rest_framework import status

# # module for authentication
# # from rest_framework import authentication
# from rest_framework import permissions


# class BookApiView(APIView):

#     def get(self, request):
#         book = BookRest.objects.all()
#         serializer = BookRestSerializer(book, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serialize = BookRestSerializer(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         return Response(serialize.data, status=status.HTTP_400_BAD_REQUEST)


# class BookApiDetail(APIView):
#     permission_classes = [permissions.IsAdminUser]
#     # authentication_classes = [authentication.TokenAuthentication]

#     def get_object(self, pk):
#         try:
#             return BookRest.objects.get(id=pk)
#         except BookRest.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookRestSerializer(book, many=False)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookRestSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from FunctionBasedRest.models import BookRest
from FunctionBasedRest.serializers import BookRestSerializer


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        book = BookRest.objects.all()
        serialize = BookRestSerializer(book, many=True)
        return Response(serialize.data)

    def create(self, request):
        serializer = BookRestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        book = BookRest.objects.get(id=pk)
        serializer = BookRestSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk):
        book = BookRest.objects.get(id=pk)
        serializer = BookRestSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk):
        book = BookRest.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
