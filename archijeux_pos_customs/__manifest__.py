# Copyright  Élabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "archijeux_pos_customs",
    "version": "16.0.1.0.1",
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
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/pos_session_view.xml",
        "views/res_partner_views.xml",        
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}