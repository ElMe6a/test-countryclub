# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Country_club_barcode(models.Model):
     _name = 'country__club.country__club'
     _description = "Country Club"
    
     countryname = fields.Char("Nombre", required=True)
     countrybarcode = fields.Char( "Codigo de Barras / Identificador", required=True )

        
        
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
