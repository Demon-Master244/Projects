from django.shortcuts import render
from django.http import HttpResponse

def lesson_4(request):
    return HttpResponse(request, 'Домашка по 4 занятию')