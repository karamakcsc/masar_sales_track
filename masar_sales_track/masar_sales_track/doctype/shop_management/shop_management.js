// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Management", {
    setup: function (frm) {
		frm.set_query("sales_man", function (doc) {
			return {
				filters: [
					['Sales Person', 'is_group', '=', 0],
					['Sales Person', 'enabled', '=', 1]
				]
			};
		});
		frm.set_query("supervisor", function (doc) {
			return {
				filters: [
					['Supervisor', 'is_enable', '=', 1]
				]
			};
		});
		frm.set_query("district", function (doc) {
			return {
				filters: [
					['District', 'is_enable', '=', 1]
				]
			};
		});
	},
});
navigator.geolocation.getCurrentPosition(function(position) {
    frappe.ui.form.on('Shop Management', {
        before_submit: function(frm) {
                var longitude = position.coords.longitude;
                var latitude = position.coords.latitude;
				console.log(longitude);
				console.log(latitude);
                frappe.call({
                    type: "GET",
                    url: `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`,
                    callback: function(r) {
						console.log(r.address);
                        frm.set_value('country', r.address.country || '');
                        frm.set_value('city', r.address.city || '');
                        frm.set_value('neighbourhood', r.address.neighbourhood || '');
                        frm.set_value('road', r.address.road || '');
                        frm.set_value('house_number', r.address.house_number || '');
                        frm.set_value('full_address', r.display_name || '');
                        frm.set_value('latitude', r.lat);
                        frm.set_value('longitude', r.lon);
                    },
                    error: function(xhr, status, error) {
                        console.log("Error fetching address from coordinates:", status, error);
                    }
                });
            
        }
    });
});