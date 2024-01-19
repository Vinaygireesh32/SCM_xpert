if (localStorage.getItem("token") === null) {
        window.location.href = "/login";
    }
document.addEventListener("DOMContentLoaded", function () {
    // Log a message to the console to indicate the script is running
    console.log("Script is running");

    // Fetch data from the "/shipmenttable" endpoint
    fetch("/shipmenttable", {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${localStorage.getItem("token")}`,
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        // Check if the response status is OK (200)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        // Parse the response as JSON
        return response.json();
    })
    .then(data => {
        console.log("Data received:", data);

        // Process the received data and generate HTML table rows
        let shipmentData = "";
        for (let shipmentSno = 0; shipmentSno < data.length; shipmentSno++) {
            const v = data[shipmentSno];
            console.log("Processing data in loop");

            // Concatenate table row HTML with shipment data
            shipmentData += `<tr><td>${shipmentSno + 1}</td>
            <td>${v.shipmentnumber}</td>
            <td>${v.containerumber}</td>
            <td>${v.routedetails}</td>
            <td>${v.goodstype}</td>
            <td>${v.device}</td>
            <td>${v.expecteddeliverydate}</td>
            <td>${v.ponumber}</td>
            <td>${v.deliverynumber}</td>
            <td>${v.ndcnumber}</td>
            <td>${v.batchid}</td>
            <td>${v.serialnumberofgoods}</td></tr>`;
            
            
        }

        // Update the content of the HTML table body with the constructed shipmentData
        document.getElementById("table-body").innerHTML = shipmentData;

        console.log("Data processing complete");
    })
    .catch(error => {
        console.error("Error fetching or processing data:", error);
    });
});
