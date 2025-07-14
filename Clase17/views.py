from django.http import HttpResponse
from django.template import Template, Context


def saludar(request):
    return HttpResponse("Mi primer mensaje")


def mayor_edad(request, edad):
    if edad >= 18:
        return HttpResponse("<h1 style='color:green'>Es mayor de edad</h1>")
    else:
        return HttpResponse("<h1 style='color:red'>Es menor de edad</h1>")
    


def probando_template(request):
    
    mi_html = open("C:/Users/Maximiliano/Desktop/Py76280/Clase17/Clase17/plantillas/template.html")
    
    plantilla = Template( mi_html.read())

    mi_html.close()

    mi_contexto = Context({"nombre":"Pepe"})

    document = plantilla.render(mi_contexto)


    return HttpResponse(document)