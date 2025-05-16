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

// frappe.ui.form.on("Airport Shop Contract", {
//     refresh: function(frm) {
//         console.log("hello world")
//     },
//     shop_details_remove: function(frm) {
//         console.log("hwllo world")
//         frappe.msgprint(__('A row has been deleted from the child table!'));
//         // You code here
//         // If you console.log(frm.doc.color) you will get the remaining color list

//         },
// });
frappe.ui.form.on("Contract Detail", {
	validate: function (frm) {
		calculate_total_rent(frm);
	},
	// shops_add: function(frm, cdt, cdn) {
	//     console.log("hello world")
	//     frappe.db.get_single_value('Airport Shop Settings', 'default_rent').then(value => {
	//         frappe.model.set_value(cdt, cdn, 'rent', value);
	//     });
	// }
	shops_on_form_rendered: function (frm, grid_row, cdt, cdn) {
		console.log("hello world");
		if (grid_row.doc.__islocal) {
			console.log("hello world");
			frappe.db.get_single_value("Airport Shop Settings", "default_rent").then((value) => {
				frappe.model.set_value(cdt, cdn, "rent", value);
			});
		}
	},
});
frappe.ui.form.on("Airport Shop Contract", {
	// this should be the child doctype name
	form_render: function (frm, cdt, cdn) {
		console.log("hello world");
	},
	refresh: function (frm) {
		console.log("hello world");
	},
	shop: function (frm, cdt, cdn) {
		// frappe.db.get_single_value('Airport Shop Settings', 'default_rent').then(value => {
		//     frappe.model.set_value(cdt, cdn, 'rent', value);
		// });
		calculate_total_rent(frm);
	},
});

// frappe.ui.form.on('Shops',{
//     shop: function(frm)
// {
//     console.log("hello world")
// }   , rent: function(frm, cdt, cdn) {
//         calculate_total_rent(frm);
//     }
// })
function calculate_total_rent(frm) {
	let ttl = 0;
	frm.doc.shops.forEach(function (s) {
		ttl += s.rent || 0;
	});
	frm.set_value("rent_amount", ttl);
}

// frappe.ui.form.on('Airport Shop Contract', {
//     shop_remove: function(frm){
//         console.log("helo world")
//     }
// })
