# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ContractDetail(Document):
	# pass
	def before_submit(self):
		invoice_doc = frappe.get_doc(
			{
				"doctype": "Airport Shop Invoice",
				"contract": self,
				"tenant": self.tenant,
				"rent_amount": self.rent_amount,
				"paid": "Unpaid",
			}
		)
		invoice_doc.insert()

	def before_save(self):
		for shop in self.shops:
			shop_doc = frappe.get_doc("Airport Shop", shop.shop)
			shop_doc.status = "Occupied"
			shop_doc.save()

	def before_cancel(self):
		for shop in self.shop_details:
			shop_doc = frappe.get_doc("Airport Shop", shop.shop)
			shop_doc.status = "Available"
			shop_doc.save()
