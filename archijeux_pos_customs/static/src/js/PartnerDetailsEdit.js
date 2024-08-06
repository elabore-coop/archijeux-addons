odoo.define("archijeux_pos_customs.PartnerDetailsEdit", function (require) {
    "use strict";

    const {useState} = owl;
    const {_t} = require("web.core");
    const PartnerDetailsEdit = require("point_of_sale.PartnerDetailsEdit");
    const Registries = require("point_of_sale.Registries");

    const PosPartnerDetailsEdit = (OriginalPartnerDetailsEdit) =>
        class extends OriginalPartnerDetailsEdit {
            setup() {
                super.setup();
                this.changes = useState({
                    ...this.changes,
                    request_to_volunteer: this.props.partner.request_to_volunteer || false,
                    request_newsletter: this.props.partner.request_newsletter || false,
                    adults_number: this.props.partner.adults_number || null,
                    children_number: this.props.partner.children_number || null,
                    other_beneficiaries_names: this.props.partner.other_beneficiaries_names || null,                    
                    free_member: this.props.partner.free_member || null,                    
                });
            }

        };

    Registries.Component.extend(PartnerDetailsEdit, PosPartnerDetailsEdit);

    return PartnerDetailsEdit;
});
