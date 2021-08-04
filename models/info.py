# -*- coding: utf-8 -*-

from odoo import models, fields,api
from datetime import date

class Card(models.Model):
    _name = 'task.info'
    # _rec_name = 'name'
    _description = 'Info'\

    @api.model
    def year_selection(self):
        year = 1990  # replace 2000 with your a start year
        year_list = []
        while year != 2030:  # replace 2030 with your end year
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    ser_type = fields.Char(string="Серия, тип проекта")
    floors = fields.Integer(string="Число этажей")
    area = fields.Integer(string="Площадь застройки")
    volume = fields.Integer(string="Объем здания")
    total_area = fields.Integer(string="Общая площадь")
    balcony_area = fields.Integer(string="Площадь балкона, лоджии и т. п.")
    living_area = fields.Integer(string="Жилая площадь")
    nonliving_area = fields.Integer(string="Площадь нежилых помещений")
    no_flats = fields.Integer(string="Число квартир")
    no_rooms = fields.Integer(string="Число помещений, комнат")
    material_walls = fields.Char(string="Материал стен")
    year = fields.Selection(
        year_selection,
        string="Год постройки",
        default="2021",  # as a default value it would be 2021
    )
    physical = fields.Char(string="Физический износ")
    date = fields.Date(string="Паспорт составлен по состоянию на", default=fields.Date.today())
                       # , default=date.year)
    # new_field = fields.Char(string="Директор")
    director = fields.Many2one('res.users', string="Директор")
