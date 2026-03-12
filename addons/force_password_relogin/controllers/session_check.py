# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SessionCheck(http.Controller):

     @http.route('/check/session', type='http', auth='public')
     def check_session(self, **kw):

        user = request.env.user

        if user.password_change_date:

            session_login = request.session.get('login_time')
            if session_login and session_login < user.password_change_date.timestamp():
                request.session.logout()
                return http.redirect_with_hash('/web/login')

        return "okaaay"