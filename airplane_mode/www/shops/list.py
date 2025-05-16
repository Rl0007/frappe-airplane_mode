import frappe

no_cache = 1


def get_context(context):
	shops = frappe.get_all(
		"Airport Shop",
		fields=["name", "shop_name", "status", "route", "area", "shop_number", "airport", "shop_image"],
	)
	context.rent = frappe.get_cached_value("Airport Shop Settings", "Airport Shop Settings", "default_rent")
	context.shops = shops
