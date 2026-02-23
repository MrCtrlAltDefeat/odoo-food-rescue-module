from odoo import models, fields

class PickupRequest(models.Model):
    _name = 'pickup_request'
    _description = 'Pickup Request'

    food_batch_id = fields.Many2one('food_batch', required=True)
    receiver_id = fields.Many2one('receiver', required=True)
    scheduled_time = fields.Datetime()
    handled_by = fields.Many2one('res.users')
