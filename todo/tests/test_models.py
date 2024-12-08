from authentication.models import User
from utils.setup_test import TestSetup
from todo.models import Todo

class TestModel(TestSetup):
    
    def test_should_create_todo(self):

        user = self.create_test_user()
       

        todo = Todo(owner=user, title="Tech Bro", description='Get the dollars')

        todo.save()

        self.assertEqual(str(todo), 'Tech Bro')

    