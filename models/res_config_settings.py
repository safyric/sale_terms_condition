from odoo import fields, models

class ResConfigSettings1(models.TransientModel):
    _inherit = 'res.config.settings'
    
    sale_note = fields.Html(related='company_id.sale_note', string="Terms & Conditions", readonly=False)
