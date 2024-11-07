from django.db import models
from django.contrib.auth.models import User
import uuid

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contraseña reseteada de {self.user.username} a las {self.created_when}"
    
class Task(models.Model):
    title = models.CharField(max_length=100)  # Campo para el título de la tarea
    completed = models.BooleanField(default=False)  # Campo para el estado de la tarea (por defecto no completada)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario


    def __str__(self):
        return self.title
    