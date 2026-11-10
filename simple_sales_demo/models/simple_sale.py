    from odoo import api, fields, models


class SimpleSale(models.Model):
    _name = 'simple.sale'
    _description = 'Simple Sale'
    _order = 'id desc'

    name = fields.Char(string='Item Name', required=True)
    quantity = fields.Float(string='Quantity', default=1.0, required=True)
    unit_price = fields.Float(string='Unit Price', required=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.depends('quantity', 'unit_price')
    def _compute_total(self):
        for record in self:
            record.total = record.quantity * record.unit_price
