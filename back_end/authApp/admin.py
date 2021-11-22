from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.habitacion import Habitacion

admin.site.register(User)
admin.site.register(Habitacion)