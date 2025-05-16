# Copyright (c) 2025, Rl0007 and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count, Sum


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()
	chart = {
		"data": {
			"labels": [x[0] for x in data],
			"datasets": [{"values": [x[1] if x[1] is not None else 0 for x in data]}],
		},
		"type": "donut",
	}

	return columns, data, None, chart, None


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Airline"),  # The name of the airline
			"fieldname": "airline",  # Matches the field alias in the query
			"fieldtype": "Link",  # Link type for the airline field
			"options": "Airline",
			"width": 200,  # Optional: specify column width
		},
		{
			"label": _("Total Revenue"),  # The total revenue for the airline
			"fieldname": "total_revenue",  # Matches the field alias in the query
			"fieldtype": "Currency",  # Use Currency type for monetary values
			"width": 150,  # Optional: specify column width
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	AirplaneTicket = DocType("Airplane Ticket")
	Flight = DocType("Airplane Flight")
	Plane = DocType("Airplane")
	query = (
		frappe.qb.from_(AirplaneTicket)
		.right_join(Flight)
		.on(AirplaneTicket.flight == Flight.name)
		.right_join(Plane)
		.on(Flight.airplane == Plane.name)
		.select(Plane.airline, Sum(AirplaneTicket.total_amount).as_("total_revenue"))
		.groupby(Plane.airline)
	)

	data = query.run()

	return data
