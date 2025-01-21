# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.full_name = self.first_name + (f" {self.last_name}" if self.last_name else "")
