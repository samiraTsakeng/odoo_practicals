# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.http import request
from odoo.exceptions import AccessDenied

class SecureSessionMixin(models.AbstractModel):
    _name = 'secure.session.mixin'

    @api.model
    def check_session_validity(self):
        """Check if user needs to re-login after password change"""
        user = request.env.user
        if user.id == 1:  # ne jamais bloquer l’admin
            return

        if user.password_change_date:
            login_time = request.session.get('login_time')
            if login_time and login_time < user.password_change_date.timestamp():
                raise AccessDenied("You need to login first")