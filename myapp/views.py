from django.shortcuts import render, HttpResponse

# Create your views here.


def text_request(request):
    return HttpResponse('You know, programming is the best!')



def my_html_request(request):
    return render(request, 'some.html')