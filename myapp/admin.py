from django.contrib import admin
from models import Size, Category, Market
from django import forms
from django.forms import ModelForm


class SizeAdminForm(forms.ModelForm):
    market = forms.MultipleChoiceField(choices = Market)
    
    class Meta:
        model = Size
        fields = "__all__"
        
    def clean_market(self):
        market = self.cleaned_data['market']
        if not market:
            raise forms.ValidationError("Choose market")

        if len(market) > 10:
            raise forms.ValidationError("Market name should be less than 10 characters")

        market = ''.join(market)
        return market


class SizeAdmin(admin.ModelAdmin):
    form = SizeAdminForm


admin.site.register(Size, SizeAdmin)
admin.site.register(Category)
