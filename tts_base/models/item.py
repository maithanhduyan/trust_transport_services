# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Item(models.Model):
    _name = 'tts.item'
    _description = 'Item Model'

    name = fields.Char('Name', index=True, required=True)
    barcode = fields.Char('Barcode')
    price = fields.Float('Price')
    url = fields.Char('Url')
    image = fields.Binary(string='Image')
    active = fields.Boolean(default=True)
    note = fields.Char('Note')
