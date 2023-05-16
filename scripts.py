from datacenter.models import Schoolkid, Lesson, Commendation


def fix_marks(schoolkid):
	bad_marks = schoolkid.mark_set.filter(points__in=[2, 3])
	for bad_mark in bad_marks:
		bad_mark.points = 5
		bad_mark.save()


def remove_chastisements(schoolkid):
	schoolkid.chastisement_set.all().delete()


def create_commendation(fio, subject_name):
	student = Schoolkid.objects.get(full_name__contains=fio)
	lesson = Lesson.objects.filter(
		subject__title=subject_name,
		year_of_study=student.year_of_study,
		group_letter=student.group_letter
	).order_by('-date').first()
	commendation = Commendation.objects.create(
		teacher=lesson.teacher,
		subject=lesson.subject,
		created=lesson.date,
		schoolkid=student,
		text='ваааай красавчик'
	)
	commendation.save()