from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    # This helps in telling the DRF on which data to retrieve from the database
    queryset = Task.objects.all().order_by("-created_at")

    # At this point we instruct the serializer on what  to use to parse the data.
    serializer_id = TaskSerializer
    serializer_class = TaskSerializer

def index(request):
    return render(request, 'tasks/index.html')