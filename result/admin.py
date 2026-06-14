from django.contrib import admin
from .models import Student, Result

# Customize Admin Panel Titles
admin.site.site_header = " Danish's Student Result Management System"
admin.site.site_title = "Student Result Admin"
admin.site.index_title = "Welcome to Student Result Dashboard"

# Register Models
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("roll_no", "name")
    search_fields = ("name", "roll_no")


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("student", "math", "science", "english")
    search_fields = ("student__name",)