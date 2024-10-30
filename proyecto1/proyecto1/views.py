from django.http import HttpResponse
import datetime

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


def fecha(request):
    
    fecha_actual= datetime.datetime.now()
    
    documento= """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" %fecha_actual
    
    return HttpResponse(documento)

def calcula_edad(request, edad, anyo):
    
    periodo= anyo-2024
    edad_anyo= edad+periodo
    documento= """<html>
    <body>
    <h1>
    En el año %s tendrás %s años.
    </h1>
    </body>
    </html>""" %(anyo, edad_anyo)
    
    return HttpResponse(documento)
    
    
    