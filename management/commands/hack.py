from django.core.management.base import BaseCommand

from scripts import Hack


class Command(BaseCommand):

    @staticmethod
    def _first_case():
        hack_1 = Hack()
        hack_1.carry_out_all_features()

    @staticmethod
    def _second_case():
        friend_fio = 'Баранова Евфросиния'
        hack_2 = Hack(friend_fio)
        hack_2.carry_out_all_features()

    @staticmethod
    def _third_case():
        fio = 'Белозеров Авдей'
        subject_name = 'Музыка'
        achievement = 'лучший'
        hack_3 = Hack(fio, subject_name, achievement)
        hack_3.carry_out_all_features()

    @staticmethod
    def _fourth_case():
        fio = 'Симён'
        hack4 = Hack(fio)
        hack4.carry_out_all_features()

    @staticmethod
    def _fourth_one_case():
        fio = ''
        hack41 = Hack(fio)
        hack41.carry_out_all_features()

    @staticmethod
    def _fourth_two_case():
        subject_name = 'матиматика'
        hack41 = Hack(subject_name=subject_name)
        hack41.carry_out_all_features()

    def handle(self, *args, **options):
        self._first_case()
        self._second_case()
        self._third_case()
        self._fourth_case()
        self._fourth_one_case()
        self._fourth_two_case()