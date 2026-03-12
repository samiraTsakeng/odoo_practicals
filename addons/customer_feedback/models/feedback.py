# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomerFeedback(models.Model):
     _name = 'customer.feedback'
     _inherit='sale.order'
     name = fields.Char(string="Feedback title")
     rating = fields.Selection([
         ('very bad', 'very bad'),
         ('bad', 'bad'),
         ('Average', 'Average'),
         ('good', 'good'),
         ('Excellent', 'Excellent')
     ], string="rate")
     comment = fields.Text(string="comment")
#customer_id = fields.Many2one(
    #'res.partner',string="Customer")
#order_id = fields.Many2one(
 #   'sale.order'
  #  ,string="Order")

