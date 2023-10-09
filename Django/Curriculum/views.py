from django.shortcuts import render

# Create your views here.
def PrimerPagina(request):
    return render(request, "main.html", {})

