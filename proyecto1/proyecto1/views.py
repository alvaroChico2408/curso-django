from django.http import HttpResponse

def saludo(request): #Primera vista
    
    documento= """<html>
    <body>
    <h1>
    Hola mundo
    </h1>
    </body>
    </html>"""
    
    
    return HttpResponse(documento)

def despedida(request): 
    
    return HttpResponse("Adiós mundo")