if (localStorage.getItem("token") === null) {
    window.location.href = "/login";
}

document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        const token = localStorage.getItem("token");
        $("#submit").on("click", function (event) {
            event.preventDefault();
            const selectDeviceId = $("#device_id").val();

            fetch("/devicedata", {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    Device_ID: selectDeviceId
                }),
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Status ${response.status}`);
                    }
                    return response.json();
                })
                .then(response => {
                    console.log(response);
                    let shipment = "";

                    for (let shipment_no = 0; shipment_no < response.data.length; shipment_no++) {
                        const ship = response.data[shipment_no];

                        shipment += "<tr><td>" +
                            ship.Device_ID + "</td><td>" +
                            ship.Battery_Level + "</td><td>" +
                            ship.First_Sensor_temperature + "</td><td>" +
                            ship.Route_From + "</td><td>" +
                            ship.Route_To + "</td></tr>";
                    }

                    // Update HTML once after the loop
                    $("#tablebody").html(shipment);
                })
                .catch(error => {
                    console.log("Error:", error.message);
                });
        });
    });
});