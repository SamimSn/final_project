from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Task

class TaskListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.task = Task.objects.create(title='Test Task', description='This is a test task', owner=self.user)

    def test_task_list_view(self):
        response = self.client.get(reverse('todo:list_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')        

    def test_task_detail_view(self):
        response = self.client.get(reverse('todo:detail', args=(self.task.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertContains(response, 'This is a test task')

    def test_task_update_view(self):
        response = self.client.get(reverse('todo:edit', args=(self.task.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertContains(response, 'This is a test task')    

    def test_task_creation(self):
        response = self.client.post(reverse('todo:list_create'), {'title': 'New Task', 'description': 'New description'})
        self.assertEqual(response.status_code, 302)
        new_task = Task.objects.get(title='New Task')
        self.assertEqual(new_task.description, 'New description')
        self.assertEqual(new_task.owner, self.user)
