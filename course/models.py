from django.db import models
from teacher.models import Teacher

# Create your models here.
class Course(models.Model):
	name=models.CharField(max_length=50)
	duration_in_months=models.SmallIntegerField()
	course_number=models.CharField(max_length=50)
	description=models.TextField(max_length=50)
	teachers=models.ForeignKey(Teacher,on_delete=models.PROTECT,blank=True,null=True)
	
	def __str__(self):
		return self.name