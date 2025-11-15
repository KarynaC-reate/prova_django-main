from django.contrib import admin
from catalogacao.models import Tipo, Genero, Documento

# Configuração para Documento (melhora a visualização no Admin)
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'get_tipo', 'data_cadastro')
    list_filter = ('genero__tipo', 'genero', 'data_cadastro')
    search_fields = ('titulo', 'conteudo')

    def get_tipo(self, obj):
        return obj.genero.tipo.nome if obj.genero and obj.genero.tipo else 'N/A'
    get_tipo.short_description = 'Tipo'

# Configuração simples para as outras entidades
admin.site.register(Tipo)
admin.site.register(Genero)