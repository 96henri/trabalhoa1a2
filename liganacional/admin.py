from django.contrib import admin

from .models import Professor
from .models import Academia
from .models import Federacao
from .models import Lutas
from .models import Aluno

admin.site.register(Professor)
admin.site.register(Academia)
admin.site.register(Federacao)
admin.site.register(Aluno)
admin.site.register(Lutas)