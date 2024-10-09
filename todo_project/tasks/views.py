from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from datetime import date  # Ensure to import the date class

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status_param = self.request.query_params.get('status')

        # Filter based on the due_date field instead of the completed property
        if status_param == 'incoming':
            return queryset.filter(due_date__gt=date.today())
        elif status_param == 'today':
            return queryset.filter(due_date=date.today())
        elif status_param == 'overdue':
            return queryset.filter(due_date__lt=date.today())
        
        return queryset

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
