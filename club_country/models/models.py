# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class club_country(models.Model):
#     _name = 'club_country.club_country'
#     _description = 'club_country.club_country'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
