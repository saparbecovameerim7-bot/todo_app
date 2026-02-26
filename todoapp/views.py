from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
  return render(request, 'index.html')

def todoAppView(request):
  all_todo_items = TodoListItem.objects.all()
  
  return render(request,'todoList.html', {'all_items': all_todo_items})

def addTodoItem(request):
  x = request.POST['content']
  new_Item = TodoListItem(content=x)
  new_Item.save()#для сохранения используется эта функция
  return HttpResponseRedirect('/todoapp/')
def deleteTodoItem(request,i):
  y = TodoListItem.objects.get(id = i)
  print(i)
  y.delete()
  return HttpResponseRedirect('/todoapp/')

def editTodoItem(request, i):
  TodoListItem.objects.update(edit = False)
  y = TodoListItem.objects.get(id = i)
  y.edit = True
  y.save()
  return HttpResponseRedirect('/todoapp/')

def saveTodoItem(requets, i):
  item = TodoListItem.objects.get(id=i)
  item.content = requets.POST['content']
  item.edit = False
  item.save()
  return HttpResponseRedirect('/todoapp/')