# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Custom field to store the Nunur size information
    nunur_size = fields.Char(
        string='Nunur Size',
        help='Custom size information for Nunur specific sales.'
    )
