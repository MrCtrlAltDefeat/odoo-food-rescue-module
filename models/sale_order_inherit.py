from odoo import api, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _auto_confirm_free_orders(self):
        domain = [
            ("amount_total", "=", 0.0),
            ("state", "in", ["draft", "sent"]),
            ("website_id", "!=", False),
        ]
        orders = self.search(domain, limit=200)
        for so in orders:
            so.action_confirm()
