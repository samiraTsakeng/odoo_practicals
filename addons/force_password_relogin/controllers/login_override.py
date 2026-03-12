from odoo.addons.web.controllers.main import Session
from odoo.http import request
from odoo import http
import time

class SessionLogin(Session):

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):

        response = super(SessionLogin, self).web_login(redirect=redirect, **kw)

        if request.session.uid:
            request.session['login_time'] = time.time()

        return response