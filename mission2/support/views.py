
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
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


class class_view(ListView):
    model = Faq
    ordering = ["-id"]
    # templates 안에 app명으로 폴더를 만든 후에, templates 네이밍을 model명_list로 하면
    # template_name을 설정안해줘도 자동으로 연결된다.
    template_name = "cbv_view.html"
