// Copyright (c) 2025, Rl0007 and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Shop Invoice", {
	refresh(frm) {
		if (frm.get_value("status") !== "Unpaid") {
			frm.add_custom_button("Mark as Paid", () => {
				frappe.msgprint({
					title: __("Mark as Paid"),
					message: __("Are you sure you want to proceed?"),
					primary_action: {
						action(values) {
							const date = new Date();
							frm.set_value("status", "Paid");
							frm.set_value("payment_date", date);
							frm.save();
						},
					},
				});
			}).addClass("btn-primary");
		}
	},
});
