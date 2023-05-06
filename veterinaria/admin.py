from django.contrib import admin

# Register your models here.


from veterinaria.models import Animal , Doctor, Consultorio


admin.site.register(Animal)
admin.site.register(Doctor)
admin.site.register(Consultorio)