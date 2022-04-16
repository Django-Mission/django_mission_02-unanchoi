
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return render(request, "index.html")


def url_view(request):
    print('url_view()')
    data = {
        "code": "1234",
        "msg": True
    }
    return JsonResponse(data)
    # return HttpResponse("<h1> hello world! <h1/>")


def url_parameter_view(request, username):
    print(f"username : {username}")
    print('url_parameter_view()')
    print(f"request.GET :  {request.GET}")  # Query String
    return HttpResponse(username)


def function_view(request):
    print(f"request.method :{request.method}")
    print(f"request.GET :{request.GET}")
    print(f"request.POST :{request.POST}")
    return render(request, 'view.html')
