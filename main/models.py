from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ------- TO DO LIST SECTION ------------- #

class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=False)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text

#----------Journal-------------#
class Note(models.Model):
    title=models.CharField(max_length=45,null=False)
    description=models.TextField(null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
	
    def __str__(self):
        return self.title
#-----------------------------#

