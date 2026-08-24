import { ReportAction } from "@web/webclient/actions/reports/report_action";
import { patch } from "@web/core/utils/patch";
import { useComponent, useEffect } from "@odoo/owl";

function toTitleCase(str) {
    return str
        .replaceAll(".", " ")
        .replace(
            /\w\S*/g,
            (txt) => `${txt.charAt(0).toUpperCase()}${txt.substr(1).toLowerCase()}`
        );
}

function mbaEnrich(component, targetElement, selector, isIFrame = false) {
    let doc = window.document;
    let contentDocument = targetElement;

    if (isIFrame) {
        contentDocument = targetElement.contentDocument;
        doc = contentDocument;
    }

    const targets = [];
    if (selector) {
        targets.push(...contentDocument.querySelectorAll(selector));
    } else {
        targets.push(contentDocument);
    }

    for (const currentTarget of targets) {
        const elementsToWrap = currentTarget.querySelectorAll("[res-model][domain], [res-model][res-id]");
        for (const element of elementsToWrap.values()) {
            if (element.closest('a[data-mba-wrapped="1"]')) {
                continue;
            }
            if (element.parentElement && element.parentElement.tagName === 'A' && element.parentElement.getAttribute('data-mba-wrapped') === '1') {
                continue;
            }

            const wrapper = doc.createElement("a");
            wrapper.setAttribute("href", "#");
            wrapper.setAttribute("data-mba-wrapped", "1");
            wrapper.addEventListener("click", (ev) => {
                ev.preventDefault();
                const resId = element.getAttribute("res-id");
                const domain = element.getAttribute("domain");
                const resModel = element.getAttribute("res-model");
                const viewType = element.getAttribute("view-type") || (resId ? "form" : "list");
                
                const action = {
                    type: "ir.actions.act_window",
                    res_model: resModel,
                    name: toTitleCase(resModel),
                    views: [
                        [false, viewType],
                        [false, viewType === "form" ? "list" : "form"],
                    ],
                };
                if (resId) {
                    action.res_id = parseInt(resId, 10);
                } else if (domain) {
                    action.domain = domain;
                }
                component.env.services.action.doAction(action);
            });
            element.parentNode.insertBefore(wrapper, element);
            wrapper.appendChild(element);
        }
    }
}

export function useMbaEnrichWithActionLinks(ref, selector = null) {
    const comp = useComponent();
    useEffect(
        (element) => {
            if (element.matches("iframe")) {
                element.addEventListener("load", () =>
                    mbaEnrich(comp, element, selector, true)
                );
            } else {
                mbaEnrich(comp, element, selector);
            }
        },
        () => [ref.el]
    );
}

patch(ReportAction.prototype, {
    setup() {
        super.setup(...arguments);
        if (this.isAccountFinancialReport) {
            useMbaEnrichWithActionLinks(this.iframe);
        }
    },
});
