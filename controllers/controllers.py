# -*- coding: utf-8 -*-
# from odoo import http


# class Horoscopo(http.Controller):
#     @http.route('/horoscopo/horoscopo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/horoscopo/horoscopo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('horoscopo.listing', {
#             'root': '/horoscopo/horoscopo',
#             'objects': http.request.env['horoscopo.horoscopo'].search([]),
#         })

#     @http.route('/horoscopo/horoscopo/objects/<model("horoscopo.horoscopo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('horoscopo.object', {
#             'object': obj
#         })

