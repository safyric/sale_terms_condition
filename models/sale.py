from odoo import fields, models

class ResCompany1(models.Model):
    _inherit = "sale.order"

    note = fields.Html('Terms and conditions', default=_default_note)
