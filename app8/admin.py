from django.contrib import admin
from app8.models import studytable,studytable1
from app8.models import PageVisit
from app8.models import Comment

# Register your models here.
admin.site.register(studytable)
admin.site.register(PageVisit)
admin.site.register(Comment)
admin.site.register(studytable1)