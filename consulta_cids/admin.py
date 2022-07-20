from django.contrib import admin

from consulta_cids.models import DoencaCategoria
from consulta_cids.models import DoencaGrupo
admin.site.register(DoencaCategoria)
admin.site.register(DoencaGrupo)
