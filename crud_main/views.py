from django.shortcuts import redirect, render
from .models import server, type_of_server,user, application, services,applicaitonshasservices, overall
from .forms import serverForm,type_of_serverForm,usersForm,serviceForm,applicationsForm,overallForm,apphasservicesForm

def index(request):
    form = serverForm()
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/index.html', context)
    
def itype_of_server(request):
    form = type_of_serverForm()
    if request.method == 'POST':
        form = type_of_serverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/type_of_server.html', context)

    
def iusers(request):
    form = usersForm()
    if request.method == 'POST':
        form = usersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/users.html', context)

def iservices(request):
    form = serviceForm()
    if request.method == 'POST':
        form = serviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/servers.html', context)

def iapphasservices(request):
    form = apphasservicesForm()
    if request.method == 'POST':
        form = apphasservicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/app_has_services.html', context)


def iapplications(request):
    form = applicationsForm()
    if request.method == 'POST':
        form = applicationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/applications.html', context)
    
def ioverall(request):
    form = overallForm()
    if request.method == 'POST':
        form = overallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/overall.html', context)


def getData(request):
    serverData = server.objects.all()
    type_of_serverData = type_of_server.objects.all()
    usersData = user.objects.all()
    serversData = services.objects.all()
    applicationsData = application.objects.all()
    applicationhasservices = applicaitonshasservices.objects.all()
    overallData = overall.objects.all()
    context = {'server':serverData,'type_of_server':type_of_serverData,'users':usersData,'servers':serversData,'applications':applicationsData,'applicationshasservices':applicationhasservices,'overall':overallData}

    return render(request, 'crud_main/get_data.html', context)

def updateServer(request, pk):
    updateObject = server.objects.get(server_id = pk)
    form = serverForm(instance=updateObject)
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)

def updateTypeOfServer(request, pk):
    updateObject = type_of_server.objects.get(type_server_id = pk)
    form = type_of_serverForm(instance=updateObject)
    if request.method == 'POST':
        form = type_of_serverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)


def updateUsers(request, pk):
    updateObject = user.objects.get(user_id = pk)
    form = usersForm(instance=updateObject)
    if request.method == 'POST':
        form = usersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)


def updateServices(request, pk):
    updateObject = services.objects.get(service_id = pk)
    form = serviceForm(instance=updateObject)
    if request.method == 'POST':
        form = serviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)


def updateApplications(request, pk):
    updateObject = application.objects.get(app_id = pk)
    form = applicationsForm(instance=updateObject)
    if request.method == 'POST':
        form = applicationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)

def updateapphasservices(request, pk):
    updateObject = applicaitonshasservices.objects.get(app_id = pk)
    form = apphasservicesForm(instance=updateObject)
    if request.method == 'POST':
        form = applicationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)



def updateOverall(request, pk):
    updateObject = overall.objects.get(id = pk)
    form = overallForm(instance=updateObject)
    if request.method == 'POST':
        form = overallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request, 'crud_main/index.html', context)

def deleteServer(request,pk):
    serverObject = server.objects.get(server_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_server.html', context)

def deleteTypeofserver(request,pk):
    serverObject = type_of_server.objects.get(type_server_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_type_of_server.html', context)

def deleteUsers(request,pk):
    serverObject = user.objects.get(user_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_users.html', context)

def deleteServices(request,pk):
    serverObject = services.objects.get(service_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_servers.html', context)

def deleteApplications(request,pk):
    serverObject = application.objects.get(app_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_apphasservices.html', context)

def deleteapphasservices(request, pk):
    serverObject = applicaitonshasservices.objects.get(app_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_applications.html', context)

def deleteOverall(request,pk):
    serverObject = overall.objects.get(id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_overall.html', context)

