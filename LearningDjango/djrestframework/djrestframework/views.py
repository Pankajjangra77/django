from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'pankaj',
            'no_of_years_active': 10,
        }
        return Response(data)