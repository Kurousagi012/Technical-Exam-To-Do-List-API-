from rest_framework import serializers
from .models import Task
from datetime import date  # Needed for date comparison

class TaskSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()  # Define 'completed' as a method field

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'completed']  # Include 'completed' in the fields

    def get_completed(self, obj):
        """ Determine the completion status based on due_date """
        if obj.due_date > date.today():
            return "Incoming"
        elif obj.due_date == date.today():
            return "Today"
        else:
            return "Overdue"
