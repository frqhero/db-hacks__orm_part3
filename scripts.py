from datacenter.models import (
	Schoolkid, Lesson, Commendation, Subject
)


class HackError(Exception):
	def __init__(self, message):
		self.message = message


class Hack:
	def __init__(
			self,
			fio='Фролов Иван',
			subject_name='Математика',
			achievement='Отлично!'
	):
		self.fio = fio
		self.subject_name = subject_name
		self.achievement = achievement
		self.set_student()
		self.set_subject()

	def set_student(self):
		if self.fio == '':
			raise HackError('Пустое имя')
		try:
			self.student = Schoolkid.objects.get(full_name__contains=self.fio)
		except Schoolkid.DoesNotExist:
			raise HackError('По указанному имени не найдено учеников')
		except Schoolkid.MultipleObjectsReturned:
			raise HackError(
				'По указанному имени найдено более одного ученика'
			)

	def set_subject(self):
		try:
			self.subject = Subject.objects.get(
				title=self.subject_name,
				year_of_study=self.student.year_of_study
			)
		except Subject.DoesNotExist:
			raise HackError('Не найдено предмета у указанного ученика')
		except Subject.MultipleObjectsReturned:
			raise HackError(
				'По указанному названию найдено более одного предмета'
			)

	def fix_marks(self):
		bad_marks = self.student.mark_set.filter(points__in=[2, 3])
		for bad_mark in bad_marks:
			bad_mark.points = 5
			bad_mark.save()

	def remove_chastisements(self):
		self.student.chastisement_set.all().delete()

	def create_commendation(self):
		lesson = Lesson.objects.filter(
			subject__title=self.subject_name,
			year_of_study=self.student.year_of_study,
			group_letter=self.student.group_letter
		).order_by('-date').first()
		commendation = Commendation.objects.create(
			teacher=lesson.teacher,
			subject=lesson.subject,
			created=lesson.date,
			schoolkid=self.student,
			text=self.achievement
		)
		commendation.save()

	def carry_out_all_features(self):
		self.fix_marks()
		self.remove_chastisements()
		self.create_commendation()
