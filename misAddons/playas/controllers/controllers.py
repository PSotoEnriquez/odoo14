# -*- coding: utf-8 -*-
# from odoo import http


# class Playas(http.Controller):
#     @http.route('/playas/playas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/playas/playas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('playas.listing', {
#             'root': '/playas/playas',
#             'objects': http.request.env['playas.playas'].search([]),
#         })

#     @http.route('/playas/playas/objects/<model("playas.playas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('playas.object', {
#             'object': obj
#         })
