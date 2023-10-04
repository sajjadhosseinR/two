from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Person, Person2
from django.contrib import messages
from .forms import CreatePersonForm , CreatePerson2Form, UpdateForm , Update2Form


# Create your views here.
def home(request):
    all = Person.objects.all()
    return render(request, 'home.html', {'all':all})

def showperson2(request):
    all = Person2.objects.all()
    return render(request, 'showperson2.html', {'all':all})

def dperson2(request,id_p):
    user = Person2.objects.get(id = id_p)
    return render(request, 'dperson2.html', {'user':user})

def p2delete(request,id_p):
    Person2.objects.get(id = id_p).delete()
    messages.success(request, 'p2 deleted', 'warning')
    return redirect('showperson2')

def p2update(request,id_p):
    user = Person2.objects.get(id = id_p)
    if request.method == 'POST':
        form = Update2Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'p2updated','warning')
            return redirect('dperson2', id_p)
    else:
        form = Update2Form(instance=user)
        return render(request,'update2.html',{'form':form})

def delete(request, id_p):
    Person.objects.get(id = id_p).delete()
    messages.success(request, message='person deleted', extra_tags='warning')
    return redirect('home')

def showhello(request):
    return render(request, 'bace.html')

def detail(request,id_p):
    user = Person.objects.get(id = id_p)
    return render(request, 'detail.html', {'user':user})

def create(request):
    if request.method == 'POST':
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Person.objects.create(name = cd['name'], family = cd['family'], age = cd['age'])
            messages.success(request,'added person', extra_tags='success')
            return redirect('home')
    else:
        form = CreatePersonForm()
    return render(request, 'create.html', {'form':form})

def create2(request):
    if request.method =='POST':
        form = CreatePerson2Form(request.POST)
        if form.is_valid():
            cleandata = form.cleaned_data
            Person2.objects.create(name = cleandata['name'], family = cleandata['family'], age = cleandata['age'])
            messages.success(request, 'p2 added', 'warning')
            return redirect('showperson2')
    else:
        form = CreatePerson2Form()
        return render(request, 'create2.html',{'form':form})

def update(request, id_p):
    person = Person.objects.get(id = id_p)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'person adede successfull', extra_tags='success')
            return redirect('detail',id_p)
    else:
        form = UpdateForm(instance=person)
        return render(request, 'update.html', {'form':form})








