from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Task(models.Model):
	text = models.CharField(max_length=120)
	details = models.TextField()
	priority = models.PositiveIntegerField(validators=[MaxValueValidator(limit_value=5), MinValueValidator(limit_value=1)])
	isCompleted = models.BooleanField()
	datetime = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-priority', '-datetime']
		verbose_name = "Tarea"
		verbose_name_plural = "Tareas"