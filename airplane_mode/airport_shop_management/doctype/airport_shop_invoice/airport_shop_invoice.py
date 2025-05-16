# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class AirportShopInvoice(Document):
	def on_submit(self):
		if self.status != "Paid":
			frappe.throw(_("Only paid invoices can be submitted"))
