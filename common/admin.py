import datetime

from django.contrib import admin
from django.utils.html import format_html

from .models import Meal,Category,OvqatImg, User
# Register your models here.

admin.site.register(User)


class ImgInlines(admin.StackedInline):
    model = OvqatImg
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','type']

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['id','name','ctg','price','get_date','get_discount','images']
    search_fields = ['id','desc']
    list_filter = ['price','created','ctg']
    list_display_links = ['id','name']
    list_per_page = 3
    inlines = [ImgInlines]


    @admin.display(empty_value='---',description='narx va skidka')
    def get_discount(self,obj):
        hisob = int(obj.price * (1 - obj.skidka/100))
        if obj.skidka:
            return format_html(
                f"<del style = 'color:red;'> {obj.price} </del><br>"
                f"<span style = 'color:green;'> {hisob}</span>"
            )
        return hisob

    @admin.display(empty_value='Rasm yoq')
    def images(self,obj):
        if obj.images.first():
            return format_html(
                f"<img src = '{obj.images.first().image.url}' width = '100px' height = '50px'>"
            )
        return "Rasm yo'q"

    @admin.display(description = 'Created')
    def get_date(self,obj):
        now = datetime.datetime.now()
        minut = int((now-obj.created).total_seconds() // 60)
        if minut == 0:
            return 'hozirgina'
        elif 0 < minut < 60:
            return f'{minut} minut oldin'
        return obj.created.strftime("%d/%m/%Y | %H:%M")
