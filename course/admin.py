from django.contrib import admin

from course.models import Student, Teacher, Major, Session, Main_unit, Public_unit, Term

admin.site.register(Major)
admin.site.register(Main_unit)
admin.site.register(Public_unit)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Term)
admin.site.register(Session)
