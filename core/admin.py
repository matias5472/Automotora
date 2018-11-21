from django.contrib import admin
from .models import Comuna, Region, TipoVivienda, Cliente, Raza, Genero, Estado, Mascota, Foto

# Register your models here.

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nomComuna', 'Region')
    search_fields = ['nomComuna', 'Region']
    list_filter = ('nomComuna', 'Region')


class mascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechaIngreso',
                    'fechaNacimiento', 'Raza', 'Genero', 'Estado', 'Foto')

    list_filter = ('Estado','Genero','Raza',)

    search_fields = ('nombre',)


class clienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nomCompleto', 'email', 'fono',
                    'fechaNaci', 'Comuna', 'TipoVivienda')
    list_filter = ('Comuna',)


class regionAdmin(admin.ModelAdmin):
    list_display = ('id','nomRegion')

    list_filter = ('nomRegion',)


admin.site.register(Region, regionAdmin)
admin.site.register(Cliente, clienteAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(TipoVivienda)
admin.site.register(Estado)
admin.site.register(Genero)
admin.site.register(Raza)
admin.site.register(Mascota, mascotaAdmin)
admin.site.register(Foto)