# -*- coding: utf-8 -*-
# from odoo import http


# class ClubCountry(http.Controller):
#     @http.route('/club_country/club_country/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/club_country/club_country/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('club_country.listing', {
#             'root': '/club_country/club_country',
#             'objects': http.request.env['club_country.club_country'].search([]),
#         })

#     @http.route('/club_country/club_country/objects/<model("club_country.club_country"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('club_country.object', {
#             'object': obj
#         })
