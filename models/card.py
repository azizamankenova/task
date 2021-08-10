# -*- coding: utf-8 -*-

from odoo import models, fields


class Card(models.Model):
    _name = 'task.card'
    # _rec_name = 'name'
    _description = 'Card'

    name = fields.Char(string="Название актива", required=True)
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
    # image = fields.Binary(string="Image", attachment=True)
    # tsel_nazn = fields.Char(string="Целевое назначение")
    # category_fond = fields.Char(string="Категория фонда")
