# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Custom field to store the Nunur size information
    nunur_size = fields.Char(
        string='Nunur Size',
        help='Custom size information for Nunur specific sales.'
    )

    # New field to store the delivery date (used in the list view)
    x_delivery_date = fields.Date(
        string='Delivery Date',
        help='Expected delivery date for the sale order.'
    )
