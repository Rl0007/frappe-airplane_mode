// Copyright (c) 2025, Rl0007 and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Contract Detail", {
// 	refresh(frm) {
//         frm.fields_dict['shop_details'].grid.wrapper.on('click', '.grid-remove-row', function() {
//             frappe.msgprint(__('A row has been deleted from the child table!'));
//             // Add your logic here
//         });
// 	},
// });

frappe.ui.form.on("Contract Detail", {
	validate: function (frm) {
		calculate_total_rent(frm);
	},
});

function calculate_total_rent(frm) {
	let ttl = 0;
	frm.doc.shops.forEach(function (s) {
		ttl += s.rent || 0;
	});
	frm.set_value("rent_amount", ttl);
}
