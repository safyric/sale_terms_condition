from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    note = fields.Html(string='Terms and conditions')
