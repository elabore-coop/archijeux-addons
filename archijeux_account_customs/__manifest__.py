# Copyright  Élabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "archijeux_account_customs",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Élabore",
    "license": "AGPL-3",
    "category": "",
    "summary": "Customs accounts dev and views for Archijeux",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "account"
    ],
    # always loaded
    "data": [
        "views/account_move_line_views.xml",
    ],
    "application": False,
}