from django.http import HttpResponse

def index(request):  #es una funcion based views (una vista basada en función)
    return HttpResponse("seticap muestra las estadísticas del precio del dólar")
