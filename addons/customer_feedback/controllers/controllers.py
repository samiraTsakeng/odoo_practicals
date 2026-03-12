# -*- coding: utf-8 -*-
from odoo import http

# class CustomerFeedback(http.Controller):
#     @http.route('/customer_feedback/customer_feedback/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_feedback/customer_feedback/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_feedback.listing', {
#             'root': '/customer_feedback/customer_feedback',
#             'objects': http.request.env['customer_feedback.customer_feedback'].search([]),
#         })

#     @http.route('/customer_feedback/customer_feedback/objects/<model("customer_feedback.customer_feedback"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_feedback.object', {
#             'object': obj
#         })