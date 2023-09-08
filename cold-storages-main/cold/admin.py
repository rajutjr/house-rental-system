from django.contrib import admin
from .models import MILL,house,adminhouses,adminhouses2,adminhouses3,excel,hello,officer

from import_export.admin import ImportExportModelAdmin

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import path
from . import views
from .form import destform

# Register your models here.


admin.site.register(adminhouses)
admin.site.register(adminhouses2)
admin.site.register(adminhouses3)
admin.site.register(hello)




#new fields 
admin.site.register(officer)

@admin.register(excel)
class student_info_resources(ImportExportModelAdmin):
    class Meta:
        model=excel

class mymodeladmin(admin.ModelAdmin):

    def get_urls(self):
        urls=super().get_urls()
        my_urls = [
            path("my_view/",self.my_view,name="my_view"),
            path("ready",views.ready,name="ready")
           
        ]   

        return my_urls + urls   
    def my_view(self,request):
        form=destform()
        
        return render(request,'adminpage.html',{"form":form,"value":admin.site.register(house)})
    
admin.site.register(MILL,mymodeladmin)