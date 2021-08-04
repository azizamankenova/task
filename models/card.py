# -*- coding: utf-8 -*-

from odoo import models, fields


class Card(models.Model):
    _name = 'task.card'
    # _rec_name = 'name'
    _description = 'Card'
    obl = fields.Char(string="Область")
    reg = fields.Char(string="Район")
    city = fields.Char(string="Город ")
    reg_in_city = fields.Char(string="Район в городе")
    address = new_field = fields.Char(string="Адрес")
    knum = fields.Integer(string="Кадастровый номер")
    inum = fields.Integer(string="Инвентарный номер")
    tsel_nazn = fields.Char(string="Целевое назначение")
    category_fond = fields.Char(string="Категория фонда")
