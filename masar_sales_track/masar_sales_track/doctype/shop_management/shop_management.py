# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class ShopManagement(Document):
	def on_submit(self):
		self.add_date_time()
  
	def add_date_time(self):
		self.date_time =  datetime.now()