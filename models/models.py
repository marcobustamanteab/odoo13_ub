# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'visit'

    name = fields.Char(string='descripciòn')
    customer = fields.Char(string='cliente')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('p', 'Presencial'), ('w', 'Whatsapp'), ('t', 'telefònico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada')

