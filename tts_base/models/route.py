# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Route(models.Model):
    _name = 'tts.route'
    _description = 'Route'

    name = fields.Char('Name', required=True)
    active = fields.Boolean(default=True)
    note = fields.Char('Note')
