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
    if _from and to:
        conditions += f" AND tse.posting_date BETWEEN '{_from}' AND '{to}'"
    
    sql = frappe.db.sql(f"""
			SELECT
				tse.sales_man AS `Sales Person`,
				tse.posting_date AS `Posting Date`,
				tse.shop_search AS `Shop Name`,
				tse.jotun_amount AS `Jotun Amount`,
				tse.uniguard_amount AS `Uniguard Amount`,
				tse.coll_amount AS `Collection Amount`,
				tse.description AS `Description`,
				tse.visit_type AS `Visit Type`
			FROM `tabShop Event` tse
			WHERE {conditions} AND tse.docstatus = 1
        """)
    
    return sql

def get_columns():
    return [
		"Sales Person: Link/Sales Person:200",
		"Posting Date: Date:200",
		"Shop Name: Link/Shop Management:200",
		"Jotun Amount: Data:200",
		"Uniguard Amount: Data:200",
		"Collection Amount: Data:200",
		"Description: Data:200",
		"Visit Type: Data:200",
	]
