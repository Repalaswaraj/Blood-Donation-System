from django.contrib import admin

# Register your models here.


from Bloodapp.models import Donar,Patient,Patientss
# Register your models here.
# class  StudentAdmin(admin.ModelAdmin):
#     list_display=['stu_name','stu_email','stu_age']
# admin.site.register(Studentss,StudentAdmin)

admin.site.register(Donar)
admin.site.register(Patient)
admin.site.register(Patientss)
