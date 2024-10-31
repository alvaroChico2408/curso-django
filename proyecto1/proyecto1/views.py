from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    
    def __init__(self,nombre,apellido):
        self.nombre= nombre
        self.apellido= apellido

def saludo(request): #Primera vista
    
    lista=["a","al","el","de"]
    lista_vacia=[]
    persona= Persona("Juan","pepe")
    fecha= datetime.datetime.now()
    nombre="pepeee"
    nombre1="holi"
    doc_externo= open("C:/Users/alvaro/Desktop/Curso Django/curso-django/proyecto1/proyecto1/plantillas/plantilla.html")
    plt= Template(doc_externo.read())
    doc_externo.close()
    ctx= Context({"nombre_persona":nombre,"nombre_persona1":nombre1, "fecha":fecha,"np":persona.nombre,"ap":persona.apellido,"lista":lista,"lista_vacia":lista_vacia})
    documento= plt.render(ctx)
    
    
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
    
    
    