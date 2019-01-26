# -*- coding: utf-8 -*-
from odoo import http

# class Luhenet(http.Controller):
#     @http.route('/luhenet/luhenet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/luhenet/luhenet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('luhenet.listing', {
#             'root': '/luhenet/luhenet',
#             'objects': http.request.env['luhenet.luhenet'].search([]),
#         })

#     @http.route('/luhenet/luhenet/objects/<model("luhenet.luhenet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('luhenet.object', {
#             'object': obj
#         })