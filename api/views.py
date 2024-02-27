from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def greetings(request):
    result = {"message":"Welcome ho raha welcome, amchya gavi welcome"}
    return JsonResponse(result)