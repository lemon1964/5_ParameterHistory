from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from .models import Parameter
from .serializers import ParameterSerializer


class ParameterView(APIView):
    queryset = Parameter.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ParameterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ParameterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parameter.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParameterSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


