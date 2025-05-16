# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

import frappe
from dateutil.relativedelta import relativedelta
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class ContractDetail(Document):
	def before_submit(self):
		start_date = getdate(self.contract_start_date)
		end_date = getdate(self.contract_expiry_date)
		current = start_date.replace(day=1)
		while current <= end_date:
			existing = frappe.db.exists(
				"Airport Shop Invoice",
				{
					"contract": self.name,
					"due_date": current,
				},
			)
			if not existing:
				invoice_doc = frappe.get_doc(
					{
						"doctype": "Airport Shop Invoice",
						"contract": self.name,
						"tenant": self.tenant,
						"rent_amount": self.rent_amount,
						"due_date": current,
						"paid": "Unpaid",
					}
				)

				invoice_doc.insert()

				# Move to the next month
			current += relativedelta(months=1)

	def before_save(self):
		for shop in self.shops:
			frappe.db.set_value("Airport Shop", shop.shop, "status", "Occupied")

	def before_cancel(self):
		for shop in self.shops:
			frappe.db.set_value("Airport Shop", shop.shop, "status", "Available")
		current_date = nowdate()
		# Delete orphan invoices
		invoices = frappe.get_all(
			"Airport Shop Invoice",
			filters={
				"contract": self.name,
				"due_date": [">=", current_date],
				"status": "Unpaid",
				"docstatus": 0,
			},
			fields=["name", "due_date"],
		)

		for invoice in invoices:
			frappe.delete_doc("Airport Shop Invoice", invoice.name)
