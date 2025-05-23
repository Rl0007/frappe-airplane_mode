# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.background_jobs import enqueue
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"

	def on_update(self):
		if self.has_value_changed("gate_number"):
			enqueue(
				method="airplane_mode.airplane_mode.api.update_gate_in_tickets.update_gate_in_tickets",
				queue="default",
				timeout=300,
				flight=self.name,
				gate_number=self.gate_number,
				now=frappe.conf.developer_mode,
			)

	def validate(self):
		if self.is_published and not self.route:
			self.route = f"flights/{self.name}"
		member_count = {"Pilot": 0, "Flight Attendant": 0, "Air Hostess": 0}
		# Check for duplicate members
		member_list = []
		airplane_settings = frappe.get_doc("Airplane Settings")
		for member in self.crew_members[:]:
			crew_doc = frappe.get_doc("Crew Member", member.crew_member)

			if str(crew_doc.name) in member_list:
				self.crew_members.remove(member)
				continue
			member_list.append(str(crew_doc.name))

			if crew_doc.airline != self.airline:
				frappe.throw(f"Crew member {crew_doc.full_name} must belong to airline {self.airline}")
			if member.designation in member_count:
				member_count[member.designation] += 1
		# Validate the counts against the limits in Airplane Settings
		if member_count["Pilot"] > airplane_settings.pilot_per_plane:
			frappe.throw(
				f"Number of pilots exceeds the allowed limit of {airplane_settings.pilot_per_plane}."
			)

		if member_count["Flight Attendant"] > airplane_settings.flight_attendant_per_plane:
			frappe.throw(
				f"Number of flight attendants exceeds the allowed limit of {airplane_settings.flight_attendant_per_plane}."
			)

		if member_count["Air Hostess"] > airplane_settings.air_hostess_per_plane:
			frappe.throw(
				f"Number of air hostesses exceeds the allowed limit of {airplane_settings.air_hostess_per_plane}."
			)
