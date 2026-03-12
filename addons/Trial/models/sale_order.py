
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit= 'sale.order'

    trial_field = fields.Selection([
        ('back_office', 'Back office'),
        ('web_site', 'Web Site')],
        string="trial field", default='back_office')

    order_channel = fields.Selection([
        ('phone', 'Phone'),
        ('website', 'Website'),
        ('store', 'Store'),
        ('whatsapp', 'Whatsapp')
    ], string="Order channel")
    internal_note = fields.Text(string="Internal note")
    priority_level = fields.Selection([
        ('low', 'low'),
        ('Normal', 'Normal'),
        ('High', 'High'),
        ('urgent', 'urgent')
    ], string="Priority level", default="High")



    @api.onchange('order_channel')
    def _onchange_order_channel(self):
        if self.order_channel == 'website':
            self.internal_note = 'Online order'
        else:
            self.internal_note = ''