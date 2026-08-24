from odoo import models, api

class AgedPartnerBalance(models.AbstractModel):
    _inherit = "report.account_financial_report.aged_partner_balance"

    def _get_partner_move_lines(self, acc_id, ag_pb_data, partners_data, journals_data, accounts_data, show_move_line_details, date_at_oject, interval_lines):
        aged_partner_data = super()._get_partner_move_lines(
            acc_id, ag_pb_data, partners_data, journals_data, accounts_data,
            show_move_line_details, date_at_oject, interval_lines
        )
        
        # Inyectar el ID del partner a partir de la comparación del nombre
        for partner_dict in aged_partner_data:
            partner_name = partner_dict.get("name")
            for prt_id, prt_info in partners_data.items():
                if prt_info.get("name") == partner_name:
                    partner_dict["id"] = prt_id
                    break
        return aged_partner_data
