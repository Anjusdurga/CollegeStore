
from .models import Departments,Courses,Purposes,Materials,Order  #import model place
from django.contrib import admin

# Register your models here.
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
admin.site.register(Departments)
admin.site.register(Courses)
admin.site.register(Purposes)
admin.site.register(Materials)
admin.site.register(Order)
# Register your models here.
