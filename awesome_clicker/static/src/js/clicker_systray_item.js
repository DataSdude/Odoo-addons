/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

class ClickerSystray extends Component {
    static template = "awesome_clicker.ClickerSystray";

    setup() {
        this.state = useState({ value: 0});
    }

    increment() {
        this.state.value = this.state.value + 1;
        if (this.props.onChange) {
            this.props.onChange();
        }
    }
}

export const systrayItem = { Component: ClickerSystray };

registry.category("systray").add("awesome_clicker.ClickerSystray", systrayItem, {
    sequence: 1
});