// Copyright (c) 2025, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Person Visits Report"] = {
	"filters": [
		{
			"fieldname": "sales_person",
			"label": __("Sales Person"),
			"fieldtype": "Link",
			"options": "Sales Person",
			"width": 100,
		},
		{
			"fieldname": "shop_name",
			"label": __("Shop Name"),
			"fieldtype": "Link",
			"options": "Shop Management",
			"width": 100,
		},
		{
			"fieldname": "from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": 80,
			// "default":  frappe.datetime.year_start()
		},
		{
			"fieldname": "to",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": 80,
			// "default":  frappe.datetime.add_days(frappe.datetime.year_start(), 30)
		},

	]
};
