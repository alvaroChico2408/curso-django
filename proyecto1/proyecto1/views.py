from django.http import HttpResponse

def saludo(request): #Primera vista
    
    return HttpResponse("Hola mundo")

def despedida(request): 
    
    return HttpResponse("Adiós mundo")