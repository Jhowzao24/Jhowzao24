from django.contrib import admin
from .models import RegisterClasses
from .forms import RegisterClassCreationForm, RegisterChangeForm
# Register your models here.

@admin.register(RegisterClasses)
class UserRegisterShow(admin.ModelAdmin):
    add_form = RegisterClassCreationForm
    form = RegisterChangeForm
    model = RegisterClasses
    list_filter = ('id', 'FullName', 'WhatsApp', 'InstrumentChoice')
    list_display = ('id', 'FullName', 'WhatsApp', 'InstrumentChoice')