from django.http import HttpResponse
def wish(request):
    message = "Hello World"
    return HttpResponse(message)
