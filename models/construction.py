# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Construction(models.Model):
    _name = 'task.construction'
    # _rec_name = 'name'
    _description = 'Construction'

    @api.model
    def default_get(self, fields):
        res = super(Construction, self).default_get(fields)
        construction_table = [(0, 0, {'sequence': 1, 'name': "Год постройки"}),
                              (0, 0, {'sequence': 2, 'name': "Протяженность дороги"}),
                              (0, 0, {'sequence': 3, 'name': "Ширина проезжей части"}),
                              (0, 0, {'sequence': 4, 'name': "Ширина тротуаров"}),
                              (0, 0, {'sequence': 5, 'name': "Ширина пешеходных дорог"}),
                              (0, 0, {'sequence': 6, 'name': "Ширина разделительной грунтовой полосы"}),
                              (0, 0, {'sequence': 7, 'name': "Ширина обочины"}),
                              (0, 0, {'sequence': 8, 'name': "Угол откоса"}),
                              (0, 0, {'sequence': 9, 'name': "Высота насыпи"}),
                              (0, 0, {'sequence': 10, 'name': "Дополнительные траспортные пути"}),
                              (0, 0, {'sequence': 11, 'name': "Количество полос"}),
                              (0, 0, {'sequence': 12, 'name': "Дорожные знаки"}),
                              (0, 0, {'sequence': 13, 'name': "Элементы освещения"}),
                              (0, 0, {'sequence': 14, 'name': "Зеленые насаждения"}),
                              (0, 0, {'sequence': 15, 'name': "Дорожные покрытия"}),
                              (0, 0, {'sequence': 16, 'name': "Электроосвещение"})]
        res.update({
            'construction_table': construction_table
        })
        return res

    # @api.model
    # def default_get(self, fields):
    #     res = super(Construction, self).default_get(fields)
    #     construction_table = [(0, 0, {'sequence': 1, 'name': "Год постройки"}),
    #                           (0, 0, {'sequence': 2, 'name': "Длина отдельных пролетов между осями опор"}),
    #                           (0, 0, {'sequence': 3, 'name': "Ширина между перилами"}),
    #                           (0, 0, {'sequence': 4, 'name': "Ширина тротуаров "}),
    #                           (0, 0, {'sequence': 5, 'name': "Высота моста"}),
    #                           (0, 0, {'sequence': 6, 'name': "Свободная высота моста"}),
    #                           (0, 0, {'sequence': 7, 'name': "Отверстие моста"}),
    #                           (0, 0, {'sequence': 8, 'name': "Отверстие пролетов"}),
    #                           (0, 0, {'sequence': 9, 'name': "Высота пролетного строения"}),
    #                           (0, 0, {'sequence': 10, 'name': "Длина пролетного строения"}),
    #                           (0, 0, {'sequence': 11, 'name': "Ширина пролетного строения"}),
    #                           (0, 0, {'sequence': 12, 'name': "Сечения пролетного строения"}),
    #                           (0, 0, {'sequence': 13, 'name': "Расстояние между осями ферм"}),
    #                           (0, 0, {'sequence': 14, 'name': "Электроосвещение"})]
    #     res.update({
    #         'construction_table': construction_table
    #     })
    #     return res

    asset_class = fields.Char(string="Класс актива")
    obl = fields.Char(string="Область")
    reg = fields.Char(string="Район")
    city = fields.Char(string="Город(поселок, населенный пункт)")
    reg_in_city = fields.Char(string="Район в городе")
    address = new_field = fields.Char(string="Адрес")
    knum = fields.Integer(string="Кадастровый номер")
    inum = fields.Integer(string="Инвентарный номер")
    pass_no = fields.Date(string="Паспорт составлен по состоянию на", default=fields.Date.today())
    director = fields.Many2one('res.users', string="Директор")
    nachalnik = fields.Many2one('res.users', string="Начальник отдела")
    ispolnitel = fields.Many2one('res.users', string="Исполнитель")
    date = fields.Date(string="Дата выдачи", default=fields.Date.today())
    construction_table = fields.One2many('task.construction.table', 'construction_id', string="")
    # tsel_nazn = fields.Char(string="Целевое назначение")
    # category_fond = fields.Char(string="Категория фонда")


class TaskConstructionTable(models.Model):
    _name = 'task.construction.table'
    _description = 'Construction table'

    sequence = fields.Integer(string="№ п/п")
    name = fields.Char(string='Наименование конструктивных элементов')
    quantity = fields.Integer(string="Количество")
    unit = fields.Char(string='Ед. измерения')
    description = fields.Char(string='Описание конструктивных элементов')
    note = fields.Char(string='Примечание')
    construction_id = fields.Many2one('task.construction', string='Construction ID')


