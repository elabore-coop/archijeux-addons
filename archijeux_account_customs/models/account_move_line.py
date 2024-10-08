from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    treated = fields.Boolean(string = 'Transmis au comptable')
