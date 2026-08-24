{
    "name": "Aged Partner Balance Drilldown",
    "version": "18.0.1.0.0",
    "category": "Accounting",
    "summary": "Adds click/drill-down links to Aged Partner Balance report",
    "author": "MBA Consultings",
    "website": "https://www.mbaconsultings.com",
    "depends": ["account_financial_report"],
    "data": [
        "report/templates/aged_partner_balance.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mba_aged_partner_balance_drilldown/static/src/js/report.esm.js",
        ],
    },
    "installable": True,
    "auto_install": False,
    "license": "AGPL-3",
}
