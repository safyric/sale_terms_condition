from odoo import fields, models

class ResCompany1(models.Model):
    _inherit = "res.company"

    sale_note = fields.Html(string='Default Terms and Conditions', translate=True)
