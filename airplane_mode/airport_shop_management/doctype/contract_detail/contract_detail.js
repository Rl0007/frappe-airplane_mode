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

// frappe.ui.form.on('Contract Detail', {
//     shop_details_remove: function(frm) {
//         // This triggers when a row is deleted from the `shop_details` child table.
//         console.log("Row deleted from shop_details");
//         console.log(frm.doc.shop_details); // Remaining rows in the child table after deletion

//         // Example: Update the total rent amount after a row is removed
//         let total_rent = 0;
//         frm.doc.shop_details.forEach((row) => {
//             total_rent += row.rent || 0; // Sum up rent from all remaining rows
//         });
//         frm.set_value('rent_amount', total_rent); // Update the rent amount in the parent DocType
//     }
// });
// frappe.ui.form.on('Airport Shop Contract', {
//     shop_remove: function(frm){
//         console.log("helo world")
//     }
// })
