from odoo import api, models, fields
from odoo.exceptions import UserError

class FoodBatch(models.Model):
    _name = 'food_batch'
    _description = 'Food Batch'

    description = fields.Char()
    quantity = fields.Float(string="Quantity Received", required=True)
    food_type = fields.Selection([('edible', 'Edible'), ('non_edible','Non-Edible')])
    expiry_date = fields.Date()
    kitchen_location = fields.Many2one(
        'stock.location', 
        string="Kitchen Location",
        required=True,
        default=lambda self: self.env.ref('stock.stock_location_stock').id
    )
    product = fields.Many2one("product.product", string="Product", required=True)
    create_uid = fields.Many2one('res.users', string='Created By', readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super(FoodBatch, self).create(vals_list)

        for rec in records:
            if not rec.product:
                raise UserError("Food batch must have a linked product to update stock.")

            # Add quantity directly to stock.quant
            quant_model = self.env['stock.quant']
            quant = quant_model.sudo().search([
                ('product_id', '=', rec.product.id),
                ('location_id', '=', rec.kitchen_location.id)
            ], limit=1)

            if quant:
                # Existing quant — just add quantity
                quant.sudo().write({'quantity': quant.quantity + rec.quantity})
            else:
                # No quant exists yet — create one
                quant_model.sudo().create({
                    'product_id': rec.product.id,
                    'location_id': rec.kitchen_location.id,
                    'quantity': rec.quantity,
                })
        return records