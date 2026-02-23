from odoo import models, fields

class ImpactLog(models.Model):
    _name = 'impact_log'
    _description = 'Impact Log'

    pickup_id = fields.Many2one('pickup_request')
    meals_saved = fields.Integer()
    kg_waste_avoided = fields.Float()
    co2_saved = fields.Float()
