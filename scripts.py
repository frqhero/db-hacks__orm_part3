from datacenter.models import Schoolkid, Lesson, Commendation, Subject


class HackError(Exception):
    def __init__(self, message):
        self.message = message


class Hack:
    def __init__(
        self,
        fio='Фролов Иван',
        subject_name='Математика',
        achievement='Отлично!',
    ):
        self.student = self.get_student(fio)
        self.subject = self.get_subject(subject_name)
        self.achievement = achievement

    @staticmethod
    def get_student(fio):
        if fio == '':
            raise HackError('Пустое имя')
        try:
            return Schoolkid.objects.get(full_name__contains=fio)
        except Schoolkid.DoesNotExist:
            raise HackError('По указанному имени не найдено учеников')
        except Schoolkid.MultipleObjectsReturned:
            raise HackError('По указанному имени найдено более одного ученика')

    def get_subject(self, subject_name):
        try:
            return Subject.objects.get(
                title=subject_name,
                year_of_study=self.student.year_of_study,
            )
        except Subject.DoesNotExist:
            raise HackError('Не найдено предмета у указанного ученика')
        except Subject.MultipleObjectsReturned:
            raise HackError(
                'По указанному названию найдено более одного предмета'
            )

    def fix_marks(self):
        self.student.mark_set.filter(points__in=[2, 3]).update(points=5)

    def remove_chastisements(self):
        self.student.chastisement_set.all().delete()

    def create_commendation(self):
        lesson = (
            Lesson.objects.filter(
                subject__title=self.subject.title,
                year_of_study=self.student.year_of_study,
                group_letter=self.student.group_letter,
            )
            .order_by('-date')
            .first()
        )
        commendation = Commendation.objects.create(
            teacher=lesson.teacher,
            subject=lesson.subject,
            created=lesson.date,
            schoolkid=self.student,
            text=self.achievement,
        )
        commendation.save()

    def carry_out_all_features(self):
        self.fix_marks()
        self.remove_chastisements()
        self.create_commendation()
