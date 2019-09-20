from django.test import TestCase
from .models import Student


class StudentTestCase(TestCase):
	def setUp(self):
		Student.objects.create(
			name='test',
			gender=2,
			email='nobody@cidp.cn',
			profession='programmer',
			tel='12345678',
		)

	def test_create_and_gender_show(self):
		student = Student.objects.create(
			name='huyang',
			gender=1,
			email='nobody@qq.com',
			profession='程序员',
			tel='2333',
		)
		self.assertEqual(student.gender, 'man', '性别字段内容与展示不一致!')

	def test_filter(self):
		Student.objects.create(
			name='huyang',
			gender=1,
			email='nobody@qq.com',
			profession='程序员',
			tel='2333'
		)
		name = 'test'
		students = Student.objects.filter(name=name)
		self.assertEqual(students.count(), 1, '应该只存在一个名为{}的记录'.format(name))
