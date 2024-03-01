if (sessionStorage.getItem("role") === "User") {
    window.location.href = "/login";
}

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
                    let deviceid = "";

                    for (let device_no = 0; device_no < response.data.length; device_no++) {
                        const dev = response.data[device_no];

                        deviceid += "<tr><td>" +
                            dev.Device_ID + "</td><td>" +
                            dev.Battery_Level + "</td><td>" +
                            dev.First_Sensor_temperature + "</td><td>" +
                            dev.Route_From + "</td><td>" +
                            dev.Route_To + "</td></tr>";
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

function logout() {
    // Clear user-related data from localStorage
    localStorage.removeItem("token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");

    // Redirect to the login page or any other desired destination
    window.location.href = "/login";
}