from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'gender', 'profession', 'email', 'tel', 'status', 'created_time')
	list_filter = ('gender', 'status', 'created_time')
	search_fields = ('name', 'profession')
	fieldsets = (
		(None, {
			'fields': (
				'name',
				('gender', 'profession'),
				('email', 'tel'),
				'status'
			)
		}),
	)


admin.site.register(Student, StudentAdmin)




