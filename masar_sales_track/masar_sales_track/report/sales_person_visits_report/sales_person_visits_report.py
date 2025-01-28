# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	return get_columns(), get_data(filters)


def get_data(filters):
    conditions = " 1=1 "
    _from , to = filters.get('from'), filters.get('to')
    if filters.get('sales_person'):
        conditions += f" AND tse.sales_man = '{filters.get('sales_person')}'"
    if filters.get('shop_name'):
        conditions += f" AND tse.shop_search = '{filters.get('shop_name')}'"
    if filters.get('status'):
        conditions += f" AND tse.status = '{filters.get('status')}'"
    if _from and to:
        conditions += f" AND tse.posting_date BETWEEN '{_from}' AND '{to}'"
    
    sql = frappe.db.sql(f"""
			SELECT
				tse.name,
				tse.sales_man AS `Sales Person`,
				tse.posting_date AS `Posting Date`,
				tsvd.duration AS `Duration`,
				tse.shop_search AS `Shop Name`,
				tse.jotun_amount AS `Jotun Amount`,
				tse.uniguard_amount AS `Uniguard Amount`,
				tse.coll_amount AS `Collection Amount`,
				tse.description AS `Description`,
				tse.visit_type AS `Visit Type`,
				tse.status AS `Status`
			FROM `tabShop Event` tse
			INNER JOIN `tabShop Visits Details` tsvd ON tse.name = tsvd.parent
			WHERE {conditions} AND tse.docstatus = 1
			GROUP BY tse.name, tsvd.duration 
        """)
    
    return sql

def get_columns():
    return [
        "Shop Event No.: Link/Shop Event:200",
		"Sales Person: Link/Sales Person:200",
		"Posting Date: Date:200",
		"Duration: Data:200",
		"Shop Name: Link/Shop Management:200",
		"Jotun Amount: Data:200",
		"Uniguard Amount: Data:200",
		"Collection Amount: Data:200",
		"Description: Data:200",
		"Visit Type: Data:200",
		"Status: Data:200",
	]
