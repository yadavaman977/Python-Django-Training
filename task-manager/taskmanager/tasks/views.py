# from django.shortcuts import render
# from django.http import HttpResponse


# def home(request):
#     return HttpResponse("<h1>Welcome to the Task Manager!</h1> <p>Here you can manage your tasks efficiently.</p>")


from django.shortcuts import render, get_object_or_404,redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    pending_count = tasks.filter(completed=False).count()
    context = {
        'tasks': tasks,
        'pending_count': pending_count,
    }
    return render(request, 'tasks/task_list.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)  # only finished tasks
    return render(request, 'tasks/task_completed.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})