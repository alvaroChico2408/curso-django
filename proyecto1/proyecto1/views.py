from django.http import HttpResponse

def saludo(request): #Primera vista
    
    return HttpResponse("<html><body><h1>Hola mundo</h1></body></html>")

def despedida(request): 
    
    return HttpResponse("Adiós mundo")