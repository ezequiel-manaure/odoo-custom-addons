/** @odoo-module **/

import { Orderline } from "@point_of_sale/app/store/models";

const SuperGetDisplayData = Orderline.prototype.getDisplayData;
Orderline.prototype.getDisplayData = function() {
    const res = SuperGetDisplayData.apply(this, arguments);
    // Añadimos el código interno del producto (default_code)
    res.default_code = this.get_product().default_code || '';
    return res;
};

