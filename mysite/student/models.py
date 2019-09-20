from django.db import models


class Student(models.Model):
	GENDER_ITEMS = [
		(1, 'man'),
		(2, 'woman'),
		(0, 'unknown')
	]
	STATE_ITEMS = [
		(0, 'apply'),
		(1, 'pass'),
		(2, 'reject')
	]

	name = models.CharField(max_length=128, verbose_name='name')
	gender = models.IntegerField(choices=GENDER_ITEMS, verbose_name='gender')
	profession = models.CharField(max_length=128, verbose_name='profession')
	email = models.EmailField(verbose_name='Email')
	tel = models.CharField(max_length=128, verbose_name='telephone')

	status = models.IntegerField(choices=STATE_ITEMS, default=0, verbose_name='Check-state')
	created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='create time')

	def __str__(self):
		return '<Student: {}>'.format(self.name)

	@classmethod
	def get_all(cls):
		return cls.objects.all()

	class Meta:
		verbose_name = verbose_name_plural = 'student information'

	@property
	def gender_show(self):
		return dict(self.GENDER_ITEMS)[self.gender]
