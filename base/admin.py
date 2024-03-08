from django.contrib import admin

# Register your models here.
# We import Room from models using . because it is in the same folder 
from .models import Room ,Topic, Message
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)

