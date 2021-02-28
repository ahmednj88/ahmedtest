from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def student_show(request):
    return render(request,'./home.html')