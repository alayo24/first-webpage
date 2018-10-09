import django
from django.shortcuts import render
from .forms import TodoAppForm
from .models import TodoApp
from django.http import HttpResponse
from .models import TodoApp
# to create a function use def and the first parameter muszt be 'request'

def index(request):
    return render(request, 'play/index.html')

def gallery(request):
    return render(request, 'play/gallery.html')



def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'play/aboutus.html')



def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'abass titi'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'apptodo/index.html', args)


def about(request):
    return render(request, 'apptodo/about.html', {})


def portfolio(request):
    return render(request, 'apptodo/portfolio.html', {})



def new_todo(request):
    todos = TodoApp.objects.all()
    if request.method == 'POST':
        if "taskadd" in request. POST:
            name = request.POST["name"]
            description = request.POST["description"]
            date = str(request.POST["date"])
            content = name + "--" + date +" " + description
            Todo = TodoApp(name=name, content=content, due_date=date, description=description)
            Todo.save()
            return redirect("/")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoApp.objects.get(id=int(todo_id))
                todo.delete()
            return redirect("/")


    return render(request, 'apptodo/new_todo.html', {'todos': todos})




def my_todos(request):
    all_my_todos = TodoApp.objects.all()
    return render(request,'apptodo/mytodos.html', {'all_my_todos':all_my_todos})


def delete_todo(request, id):
    TodoApp.objects.get(pk=id).delete()
    return render(request,'apptodo/index.html')

def edit_todo(request, id):
    if request.method == 'POST':
        form = TodoAppForm(request.POST, isinstance=request.TodoApp)
        if form.is_valid():
            form.save()
            return render(request, 'apptodo/edit_todo.html')
    else:
       # form = TodoAppForm(isinstance =request.TodoApp)
        #args ={'form' : form}
        return render (request,'apptodo/mytodos.html')


#TodoApp.objects.get(pk=id).edit()
   # request.POST.get()
   # return render(request, 'amytodos.html')






#i noticed we change the index to base in views
"""to active do django>myvenv\Scripts\activate
to run Todoapp>python manage.py runserver u
inside objects u add anything eg .5 ie the first 5,_date_added ie according to time
"""



