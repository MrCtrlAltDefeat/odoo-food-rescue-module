from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_leftover = fields.Boolean(
        string="Is Leftover Food?",
        help="Mark to publish this as a leftover item for NGOs."
    )
    food_type = fields.Selection(
        [
            ("fruit_veg", "Fruits & Vegetables"),
            ("cooked", "Cooked Meals"),
            ("bakery", "Bakery"),
            ("dairy", "Dairy"),
            ("protein", "Protein"),
            ("other", "Other"),
        ],
        string="Food Type",
    )
    leftover_qty = fields.Float(string="Leftover Quantity")
    leftover_qty_unit = fields.Selection(
        [
            ("kg", "Kg"),
            ("g", "g"),
            ("people", "People it can feed"),
        ],
        string="Quantity Unit",
        default="kg",
    )

   
