from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    note = fields.Html('Terms and conditions')
