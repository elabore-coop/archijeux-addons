from odoo import _, fields, models
from odoo.exceptions import UserError

class PosSession(models.Model):
    _inherit = "pos.session"

    number_of_major_visitors = fields.Integer('Number of major visitors')
    number_of_minor_visitors = fields.Integer('Number of minor visitors')
    benevoles = fields.Char('Bénévoles qui ont tenu la caisse')

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

    #overwrite
    #TODO : attention update_closing_control_state_session est aussi surchargé dans le module pos_daily_sales_reports, à prendre en compte si le module est installé
    def update_closing_control_state_session(self, notes, number_of_major_visitors = None, number_of_minor_visitors = None, benevoles = None):
        # Prevent closing the session again if it was already closed
        if self.state == 'closed':
            raise UserError(_('This session is already closed.'))
        # Prevent the session to be opened again.
        self.write({'state': 'closing_control',
                    'stop_at': fields.Datetime.now(),
                    'number_of_major_visitors': number_of_major_visitors,
                    'number_of_minor_visitors': number_of_minor_visitors,
                    'benevoles': benevoles,
                    })
        self._post_cash_details_message('Closing', self.cash_register_difference, notes)