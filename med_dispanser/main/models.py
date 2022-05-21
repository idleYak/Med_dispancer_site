from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Service = main_services
Symbol = service_symbols
Receipt = times_of_receipt
Talon = talons
"""


class Symbol(models.Model):
    symbol = models.CharField ('Буква-символ отделения', max_length=1)

    def __str__(self):
        return self.symbol

class Service(models.Model):
    name_service = models.CharField('Наименование услуги', max_length=100)
    open_service = models.BooleanField('Наличие услуги')
    start_hospitalization = models.TimeField('Начало времени приёма')
    end_hospitalization = models.TimeField('Конец времени приёма')
    start_button = models.TimeField('Начало времени работы кнопки')
    end_button = models.TimeField('Конец времени работы кнопки')
    id_symbol = models.ForeignKey(Symbol, on_delete = models.CASCADE)

    def __str__(self):
        return self.name_service

class Receipt(models.Model):
    start_time = models.TimeField('Время начала приёма')
    end_time = models.TimeField('Время конца приёма')

    def __str__(self):
        st = self.start_time.strftime("%H:%M")
        et = self.end_time.strftime("%H:%M")
        return st+'-'+et

class Talon(models.Model):
    id_service = models.ForeignKey(Service, on_delete = models.CASCADE)
    id_time_of_receipt = models.ForeignKey(Receipt, on_delete = models.CASCADE)
    condition = models.IntegerField('Состояние талона', default=0, validators=
    [MaxValueValidator(2), MinValueValidator(0)])
    time_registration = models.TimeField('Время регистрации', default='00:00:00')

    def __str__(self):
        ids = str(self.id_service)
        idt = str(self.id_time_of_receipt)
        idtal = str(self.id) + str(self.id_service.id_symbol)
        return idtal + ' ' + ids + ' ' + idt
