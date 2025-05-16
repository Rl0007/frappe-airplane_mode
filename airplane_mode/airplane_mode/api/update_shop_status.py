import frappe
from frappe.utils import nowdate


def update_shop_status_for_expired_contracts():
	expired_contracts = frappe.get_all(
		"Contract Detail", filters={"contract_expiry_date": nowdate()}, fields=["name"]
	)
	expired_contracts = [contract["name"] for contract in expired_contracts]
	shops = frappe.get_all(
		"Airport Shop Contract", filters={"parent": ["in", expired_contracts]}, fields=["name", "shop"]
	)
	for shop in shops:
		frappe.set_value("Airport Shop", shop.shop, "status", "Available")
