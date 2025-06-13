from frappe import _

def get_data():
    return [
        {
            "module_name": "SourcingManager",
            "label": _("Sourcing Manager"),
            "color": "#34a853",
            "icon": "octicon octicon-package",
            "type": "module",
            "description": _("Manage sourcing item requests and supplier follow-up."),
            "items": [
                {
                    "type": "doctype",
                    "name": "Sourcing Request",
                    "label": _("Sourcing Request"),
                },
                {
                    "type": "doctype",
                    "name": "Requested Item",
                    "label": _("Requested Item"),
                },
                {
                    "type": "doctype",
                    "name": "Supplier Info",
                    "label": _("Supplier Info"),
                },
                {
                    "type": "doctype",
                    "name": "Sourcing Quotation",
                    "label": _("Sourcing Quotation"),
                }
            ]
        }
    ]
