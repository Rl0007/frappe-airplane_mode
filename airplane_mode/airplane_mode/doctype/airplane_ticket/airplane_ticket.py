# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

import random
import string

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		flight_doc = frappe.get_doc("Airplane Flight", self.flight)
		airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)
		ticket_count = frappe.db.count("Airplane Ticket")
		if ticket_count >= airplane_doc.capacity:
			frappe.throw(f"Max capacity of {airplane_doc.capacity} reached!!!")

		total_amount = self.flight_price
		items_list = []

		for add_on in self.add_ons[:]:
			if add_on.item in items_list:
				self.add_ons.remove(add_on)
				# continue
			else:
				items_list.append(add_on.item)
				total_amount += add_on.amount
		self.total_amount = total_amount

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Passenger has not boarded yet, change the status to boarded to continue..")

	def populate_seat(self):
		if not self.seat:
			self.seat = f"{random.randint(0,100)}{random.choice(string.ascii_uppercase[:5])}"

	def before_save(self):
		self.populate_seat()
