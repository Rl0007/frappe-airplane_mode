// Copyright (c) 2025, Rl0007 and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Shop Invoice", {
	refresh(frm) {
		// frm.add_custom_button("Mark as Paid",()=>{
		//     frm.set_value("status","Paid")
		//     frm.save()
		// })
		if (frm.get_value("status") !== "Unpaid") {
			frm.add_custom_button("Mark as Paid", () => {
				// // Create a dialog
				// const dialog = new frappe.ui.Dialog({
				// 	title: "Mark as Paid",

				// 	primary_action_label: "Mark as Paid",
				// 	primary_action: function (data) {
				// 		// Set the entered seat number to the 'Seat' field in the form
				// 		// frm.set_value("seat", data.seat_number);
				//         frm.set_value("status","Paid")
				//             frm.save()
				// 		dialog.hide();
				// 	},
				// });

				// // Show the dialog
				// dialog.show();
				frappe.msgprint({
					title: __("Mark as Paid"),
					message: __("Are you sure you want to proceed?"),
					primary_action: {
						action(values) {
							// console.log(values);
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
