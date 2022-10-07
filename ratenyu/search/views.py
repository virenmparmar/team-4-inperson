from django.http import HttpResponse


def index(request):
    return HttpResponse("This is our homepage/search page.")

