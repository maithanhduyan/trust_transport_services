# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Parcel(models.Model):
    _name = 'tts.parcel'
    _description = 'Parcel'

    tracking_code = fields.Char(
        'TrackingCode', required=True)
    active = fields.Boolean(default=True)
    customer = fields.Many2one(
        'res.partner', string='Customer', on_delete='restrict')
    note = fields.Char('Note')
