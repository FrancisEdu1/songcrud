from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def play_song(request):
    return HttpResponse('DJ Play My Song')