from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    computer_generation = fields.Char(string='Computer Generation')