from django.contrib import admin
from myapp.models import Parents, Person, Student


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','details']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','details','college','age']


@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'details', 'related_to', 'relationship']
