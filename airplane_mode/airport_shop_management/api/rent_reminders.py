import frappe
from frappe.query_builder import DocType
from frappe.utils import formatdate, nowdate


def send_rent_due_reminders():
	send_reminder = frappe.get_cached_value(
		"Airport Shop Settings", "Airport Shop Settings", "send_rent_remainder"
	)
	if not send_reminder:
		return
	unpaid_invoices = get_unpaid_invoices()
	for invoice in unpaid_invoices:
		if not invoice.email:
			continue  # Skip if no email

		subject = f"Rent Due Reminder for {formatdate(invoice.due_date, 'MMMM yyyy')}"
		message = f"""
        Dear {invoice.full_name},

        This is a friendly reminder that your rent of ₹{invoice.rent_amount} is due for the month of {formatdate(invoice.due_date, 'MMMM yyyy')}.

        Please make the payment at your earliest convenience.

        Regards,
        Airport Management
        """

		frappe.sendmail(recipients=invoice.email, subject=subject, message=message)


def get_unpaid_invoices():
	shop_invoice = DocType("Airport Shop Invoice")
	contract = DocType("Contract Detail")
	tenant = DocType("Tenant")
	today = nowdate()

	query = (
		frappe.qb.from_(shop_invoice)
		.left_join(contract)
		.on(shop_invoice.contract == contract.name)
		.left_join(tenant)
		.on(contract.tenant == tenant.name)
		.where(shop_invoice.status == "Unpaid" and shop_invoice.due_date <= today)
		.select(shop_invoice.due_date, tenant.full_name, tenant.email, shop_invoice.rent_amount)
	)
	data = query.run(as_dict=True)
	return data
