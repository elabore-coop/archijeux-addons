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
                    adults_number: this.props.partner.adults_number || 0,
                    children_number: this.props.partner.children_number || 0,
                    other_beneficiaries_names: this.props.partner.other_beneficiaries_names || null,                    
                    free_member: this.props.partner.free_member || null,                    
                });
            }

            saveChanges() {
                const processedChanges = {};
                for (const [key, value] of Object.entries(this.changes)) {
                    if (this.intFields.includes(key)) {
                        processedChanges[key] = parseInt(value, 10) || false;
                    } else {
                        processedChanges[key] = value;
                    }
                }
                // DO NOT MAKE INTERGER FIELDS MANDATORY BECAUSE ODOO DOESNT MAKE THE DIFFERENCE BETWEEN 0 AND NULL
                // if (((!this.props.partner.adults_number || this.props.partner.adults_number == "") && !processedChanges.adults_number) || !processedChanges.adults_number)
                //     {
                //     return this.showPopup("ErrorPopup", {
                //         title: _t("Field Adulte number is required"),
                //     });
                // }
                // if (((!this.props.partner.children_number || this.props.partner.children_number == "") && !processedChanges.children_number) || !processedChanges.children_number)
                //     {
                //     return this.showPopup("ErrorPopup", {
                //         title: _t("Field Children number is required"),
                //     });
                // }
                if (((!this.props.partner.email || this.props.partner.email == "") && !processedChanges.email) || !processedChanges.email)
                    {
                    return this.showPopup("ErrorPopup", {
                        title: _t("Field Email is required"),
                    });
                }

                if (((!this.props.partner.zip || this.props.partner.zip == "") && !processedChanges.zip) || !processedChanges.zip)
                    {
                    return this.showPopup("ErrorPopup", {
                        title: _t("Field ZIP is required"),
                    });
                }

                if (((!this.props.partner.city || this.props.partner.city == "") && !processedChanges.city) || !processedChanges.city)
                    {
                    return this.showPopup("ErrorPopup", {
                        title: _t("Field City is required"),
                    });
                }
                super.saveChanges();
            }

        };

    Registries.Component.extend(PartnerDetailsEdit, PosPartnerDetailsEdit);

    return PartnerDetailsEdit;
});
