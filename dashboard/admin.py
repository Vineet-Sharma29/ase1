from django.contrib import admin
from .models import Marks
from .models import csvfile
from .models import Enrollments
from .models import course_dashboard

admin.site.register(csvfile)
admin.site.register(Marks)
admin.site.register(Enrollments)
admin.site.register(course_dashboard)