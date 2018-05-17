from django.contrib import admin
from pepito.models import Registrado


class AdminRegistrado(admin.ModelAdmin):
    list_display = ['__str__', 'nombre', 'timestamp']
    list_filter = ['timestamp']
    list_editable = ['nombre']
    search_fields = ['email', 'nombre']

    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminRegistrado)
