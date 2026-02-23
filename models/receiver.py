from odoo import models, fields

class Receiver(models.Model):
    _name = 'receiver'
    _description = 'Receiver (NGO or Employee)'

    name = fields.Char(required=True)
    contact = fields.Char()
    pickup_capacity = fields.Integer()
    user_id = fields.Many2one('res.users')
