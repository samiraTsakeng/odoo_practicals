# -*- coding: utf-8 -*-
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    password_change_date = fields.Datetime("Password Change Date")

    def write(self, vals):
        """Store the datetime when password is changed"""
        if 'password' in vals:
            vals['password_change_date'] = fields.Datetime.now()
        return super(ResUsers, self).write(vals)