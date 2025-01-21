import frappe


def execute():
	tickets = frappe.db.get_all("Airplane Ticket")
	for ticket in tickets:
		ticket_obj = frappe.get_doc("Airplane Ticket", ticket)
		if ticket_obj.seat is None:
			ticket_obj.populate_seat()
			ticket_obj.save()
	frappe.db.commit()
