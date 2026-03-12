# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    password_change_date = fields.Datetime(string='Password changed date')

    def write(self, vals):
        if 'password' in vals:
            vals['password_change_date'] = fields.datetime.now()

        return super(ResUsers, self).write(vals)
