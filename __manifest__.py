{
    "name": "Aged Partner Balance Drilldown (MBA Consultings)",
    "version": "18.0.1.0.3",
    "category": "Accounting",
    "summary": "Adds click/drill-down links to Aged Partner Balance report | MBA Consultings",
    "author": "MBA Consultings, Brooks Gonzalez",
    "website": "https://mbaconsultings.com",
    "depends": ["account_financial_report"],
    "data": [
        "report/templates/aged_partner_balance.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mba_aged_partner_balance_drilldown/static/src/js/report.esm.js",
            "mba_aged_partner_balance_drilldown/static/src/css/report.css",
        ],
    },
    "installable": True,
    "auto_install": False,
    "license": "AGPL-3",
}
