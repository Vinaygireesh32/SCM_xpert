if (sessionStorage.getItem("role") === "User") {
    window.location.href = "/login";
}

if (localStorage.getItem("token") === null) {
    window.location.href = "/login";
}


$(document).ready(function(){
    

    console.log("Token:", `${localStorage.getItem("token")}`);
   
    // Check if token exists and not expired
   
        fetch(`/shipmenttable`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`,
                'Content-Type': 'application/json',
            },
        })
        .then(response => {
          console.log("Response Status:", response.status);
     
          // Check if the response status is 401 (Unauthorized)
     
          // Continue processing for other response statuses
          if (response.status !== 200) {
              throw new Error(`Status ${response.status}`);
          }
     
          return response.json();
      })
        .then(response => {
            console.log("API Response:", response);
            if (response.status_code === 400) {
                console.log("Error:", response.detail);
                $("#error").text(response.detail);
            }
   
            let shipment_data = "";
            for (let shipment_no = 0; shipment_no < response.length; shipment_no++) {
                const shipment = response[shipment_no];
   
                shipment_data = shipment_data + "<tr><td>"
                    + shipment.username + "</td><td>"
                    + shipment.shipmentnumber + "</td><td>"
                    + shipment.containerumber + "</td><td>"
                    + shipment.routedetails + "</td><td>"
                    + shipment.goodstype + "</td><td>"
                    + shipment.device + "</td><td>"
                    + shipment.expecteddeliverydate + "</td><td>"
                    + shipment.ponumber + "</td><td>"
                    + shipment.deliverynumber + "</td><td>"
                    + shipment.ndcnumber + "</td><td>"
                    + shipment.batchid + "</td><td>"
                    + shipment.serialnumberofgoods + "</td><td>"
                    + shipment.shipmentdescription + "</td></tr>";
            }
   
            console.log("Shipment Data:", shipment_data);
            $("#table").html(shipment_data);
        })
        .catch(error => {
            console.log("Error:", error.message);
            // Check if the error is due to token expiration
          
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