from django import forms
from .models import Category,Meal


class Ctgform(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"