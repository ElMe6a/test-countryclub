# -*- coding: utf-8 -*-
# from odoo import http


# class CountryClub(http.Controller):
#     @http.route('/country__club/country__club/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/country__club/country__club/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('country__club.listing', {
#             'root': '/country__club/country__club',
#             'objects': http.request.env['country__club.country__club'].search([]),
#         })

#     @http.route('/country__club/country__club/objects/<model("country__club.country__club"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('country__club.object', {
#             'object': obj
#         })
