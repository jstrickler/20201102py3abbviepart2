from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django World", 203)

