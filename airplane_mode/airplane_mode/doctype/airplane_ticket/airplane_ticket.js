// Copyright (c) 2025, Rl0007 and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh: function (frm) {
		// Add a custom button to open the dialog
		frm.add_custom_button("Assign Seat", () => {
			// Create a dialog
			const dialog = new frappe.ui.Dialog({
				title: "Select Seat",
				fields: [
					{
						label: "Seat Number",
						fieldname: "seat_number",
						fieldtype: "Data",
					},
				],
				primary_action_label: "Assign",
				primary_action: function (data) {
					// Set the entered seat number to the 'Seat' field in the form
					frm.set_value("seat", data.seat_number);
					dialog.hide();
				},
			});

			// Show the dialog
			dialog.show();
		}).addClass("btn-primary");
	},
});
