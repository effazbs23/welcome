# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nunur_size = fields.Char(string='Nunur Size')
