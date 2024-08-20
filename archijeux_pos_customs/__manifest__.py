# Copyright  Élabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "archijeux_pos_customs",
    "version": "16.0.1.0.3",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Élabore",
    "license": "AGPL-3",
    "category": "",
    "summary": "Customs dev and views for Archijeux",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "point_of_sale",
        "membership",
        "membership_extension"
    ],
    # always loaded
    "data": [
        "views/pos_session_view.xml",
        "views/res_partner_views.xml",        
    ],
    "assets": {
        "point_of_sale.assets": [
            "archijeux_pos_customs/static/src/css/pos_archijeux_custom.css",
            "archijeux_pos_customs/static/src/xml/PartnerDetailsEdit.xml",
            "archijeux_pos_customs/static/src/js/PartnerDetailsEdit.js",
        ]
    },
    "application": False,
}