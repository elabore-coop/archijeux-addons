from odoo import fields, models


class PosSession(models.Model):
    _inherit = "pos.session"

    number_of_major_visitors = fields.Integer('Number of major visitors')
    number_of_minor_visitors = fields.Integer('Number of minor visitors')

    def _loader_params_res_partner(self):
        res = super()._loader_params_res_partner()
        res["search_params"]["fields"] += [
            "request_to_volunteer",
            "request_newsletter",
            "adults_number",
            "children_number",
            "other_beneficiaries_names",
            "free_member",
        ]
        return res