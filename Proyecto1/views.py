from django.http import HttpResponse
from django.template import Template, context, loader

def probandohtml(request):
    diccionario={"nombre":"Juan","apellido":"Perez","edad":25}
    
    contexto=context(diccionario)
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    