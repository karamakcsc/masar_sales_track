# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	return get_columns(), get_data(filters)


def get_data(filters):
    conditions = " 1=1 "
    _from , to = filters.get('from'), filters.get('to')
    if _from and to:
        conditions += f" AND tse.posting_date BETWEEN '{_from}' AND '{to}'"
    
    sql = frappe.db.sql(f"""
            SELECT 
				tse.sales_man AS `Sales Man`,
				COUNT(tse.name) AS `Number of Visits`,
				SUM(tse.jotun_amount) AS `Jotun Amount`,
				SUM(tse.uniguard_amount) AS `Uniguard Amount`,
				SUM(tse.coll_amount) AS `Collection Amount`
			FROM `tabShop Event` tse
			WHERE {conditions} AND tse.docstatus = 1
			GROUP BY tse.sales_man 
		""")
    
    return sql

def get_columns():
    return [
		"Sales Man: Link/Sales Person:200",
		"Number of Visits: Data:200",
		"Jotun Amount: Data:200",
		"Uniguard Amount: Data:200",
		"Collection Amount: Data:200",
	]
