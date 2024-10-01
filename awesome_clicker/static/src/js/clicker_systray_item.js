/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, useExternalListener } from "@odoo/owl";

class ClickerSystray extends Component {
    static template = "awesome_clicker.ClickerSystray";

    setup() {
        this.state = useState({ value: 0});
        useExternalListener(document.body, "click", (ev) => {
            this.increment(ev);
        }, {capture: true});
    }

    increment(ev) {
        console.log(ev.target.id);
        if (ev.target.id === 'btn'){
            this.state.value = this.state.value + 10;
        }else{
            this.state.value = this.state.value + 1;
        }
        
        if (this.props.onChange) {
            this.props.onChange();
        }
    }
}

export const systrayItem = { Component: ClickerSystray };

registry.category("systray").add("awesome_clicker.ClickerSystray", systrayItem, {
    sequence: 100
});