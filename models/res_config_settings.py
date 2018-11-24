from odoo import fields, models

class CompanyInfo(models.Model):
    _inherit = 'res.config.settings'
    
    sale_note = fields.Html(related='company_id.sale_note', string="Terms & Conditions")
