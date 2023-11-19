from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def administrador (request):
     return render (request, "core/administrador.html")

def secretaria (request):
     return render (request, "core/secretaria.html")

def paciente(request):
     return render (request, "core/paciente.html")

def medico (request):
     return render (request, "core/medico.html")

def cajero(request):
     return render (request, "core/cajero.html")

def home(request):
    return render(request, "core/home.html")

def calendario (request):
    return render(request,"core/calendario.html")


def Usuario(request, action, id):
    data = {"mesg": "", "form": UsuarioForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = UsuarioForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El usuario fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos usuarios con el mismo rut!"

    elif action == 'upd':
        objeto = Usuario.objects.get(rut=id)
        if request.method == "POST":
            form = UsuarioForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El usuario fue actualizado correctamente!"
        data["form"] = UsuarioForm(instance=objeto)

    elif action == 'del':
        try:
            Usuario.objects.get(rut=id).delete()
            data["mesg"] = "¡El Usuario fue eliminado correctamente!"
            return redirect(Usuario, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"

    data["list"] = Usuario.objects.all().order_by('rut')
    return render(request, "core/admin.html", data)


def poblar_bd(request):
   
    return redirect(Usuario, action='ins', id = '-1')




