from odoo import models, api

class AgedPartnerBalance(models.AbstractModel):
    _inherit = "report.account_financial_report.aged_partner_balance"

    def _create_account_list(
        self,
        ag_pb_data,
        accounts_data,
        partners_data,
        journals_data,
        show_move_line_details,
        date_at_oject,
    ):
        aged_partner_data = super()._create_account_list(
            ag_pb_data,
            accounts_data,
            partners_data,
            journals_data,
            show_move_line_details,
            date_at_oject,
        )
        for account in aged_partner_data:
            for partner in account.get("partners", []):
                partner_name = partner.get("name")
                for prt_id, prt_info in partners_data.items():
                    if prt_info.get("name") == partner_name:
                        partner["id"] = prt_id
                        break
        return aged_partner_data
