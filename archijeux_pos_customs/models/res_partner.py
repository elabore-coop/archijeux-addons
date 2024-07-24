# Copyright 2024 Elabore (https://elabore.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    request_newsletter = fields.Boolean("I want to receive the newsletter")
    request_to_volunteer = fields.Boolean("I want to volunteer")

    children_number = fields.Integer("Number of children in the household", help="For family memberships, enter the number of minors who will benefit from the membership.")
    adults_number = fields.Integer("Number of adults in the household", help="For family memberships, enter the number of adults who will benefit from the membership.")
