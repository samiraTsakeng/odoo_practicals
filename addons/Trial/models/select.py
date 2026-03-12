# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TrialSelect(models.Model):
     _name = 'trial.select'

     name = fields.Selection([('back_office', 'Back office'),
                              ('Site_web', 'Site web')],
                             string='nom', default='back_office')
    # value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100