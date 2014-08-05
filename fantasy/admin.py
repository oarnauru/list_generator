from django.contrib import admin
from fantasy.models import *
from django.forms import CheckboxSelectMultiple



class ReglaAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'short_description')


class ArmaAdmin(admin.ModelAdmin):
    list_display = ('name', 'race')

class EquiposAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'race', 'puntos')

class ArmaMagicaAdmin(EquiposAdmin):
    pass

class ArmaduraAdmin(EquiposAdmin):
    pass

class ArmaduraMagicaAdmin(EquiposAdmin):
    pass

class TalismanAdmin(EquiposAdmin):
    pass

class EstandarteMagicoAdmin(EquiposAdmin):
    pass

class ObjetoArcanoAdmin(EquiposAdmin):
    pass

class ObjetoHechizadoAdmin(EquiposAdmin):
    pass

'''
class UnidadAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class HechizoAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'dificultad')


class HechizoInline(admin.StackedInline):
    model = Hechizo
    extra = 1

class SaberAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'get_hechizos')

    inlines = [HechizoInline]

'''

admin.site.register(Regla, ReglaAdmin)
admin.site.register(Arma, ArmaAdmin)
admin.site.register(ArmaMagica, ArmaMagicaAdmin)
admin.site.register(Armadura, ArmaduraAdmin)
admin.site.register(ArmaduraMagicas, ArmaduraMagicaAdmin)
admin.site.register(Talisman, TalismanAdmin)
admin.site.register(ObjetoArcano, ObjetoArcanoAdmin)
admin.site.register(ObjetoHechizado, ObjetoHechizadoAdmin)
admin.site.register(EstandarteMagico, EstandarteMagicoAdmin)
'''
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Hechizo, HechizoAdmin)
admin.site.register(Saber, SaberAdm
admin.site.register(Montura)
admin.site.register(Tropa)
admin.site.register(Magia)in)
'''