# -*- coding: utf-8 -*-
# from odoo import http


# class Ocio(http.Controller):
#     @http.route('/ocio/ocio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ocio/ocio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ocio.listing', {
#             'root': '/ocio/ocio',
#             'objects': http.request.env['ocio.ocio'].search([]),
#         })

#     @http.route('/ocio/ocio/objects/<model("ocio.ocio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ocio.object', {
#             'object': obj
#         })
