from django.contrib import admin
from .models import Project
from .models import Reviewer
from .models import Supervisor
from .models import Project_Reviews

admin.site.register(Project)
admin.site.register(Reviewer)
admin.site.register(Supervisor)
admin.site.register(Project_Reviews)

