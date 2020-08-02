from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     DestroyAPIView,
#     UpdateAPIView,
#     CreateAPIView
# )

from .models import Task
from .serializers import TaskSerializers


class TaskViewSets(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()

def apiOverview(request):
    api_urls ={
        'List' : '/task/list/',
        'Detail View' : '/task-detail/<str:pk>/' ,
        'Create' : '/task-create/' ,
        'Update' : '/task-update/<str:pk>/' ,
        'Delete' : '/task-delete/<str:pk>/' , 
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializers(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task - Task.objects.get(id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    

    return Response("Item succesfully deleted")

                                                    ############################
                                                    ###   Class Based View   ###
                                                    ############################


# class TaskList(ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
    

# class TaskCreate(CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
    

# class TaskDetail(RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
    

# class TaskUpdate(UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
    

# class TaskDelete(DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
    