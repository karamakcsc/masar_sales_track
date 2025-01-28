// Copyright (c) 2025, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Cumulative Sales Person Visits Report"] = {
	"filters": [
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
