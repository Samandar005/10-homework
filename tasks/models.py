from django.db import models
from django.shortcuts import reverse


class Task(models.Model):
    tasks_title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    description = models.TextField()

    def get_detail_url(self):
        return reverse('tasks:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('tasks:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('tasks:delete', args=[self.pk])