// document.addEventListener("DOMContentLoaded", function () {
//     // Log a message to the console to indicate the script is running
//     console.log("Script is running");

//     // Fetch data from the "/shipmenttable" endpoint
//     fetch("/myshipment", {
//         method: 'GET',
//         headers: {
//             'Authorization': `Bearer ${localStorage.getItem("token")}`,
//             'Content-Type': 'application/json',
//         },
//     })
//         .then(response => {
//             // Check if the response status is OK (200)
//             if (!response.ok) {
//                 throw new Error(`HTTP error! Status: ${response.status}`);
//             }
//             // Parse the response as JSON
//             return response.json();
//         })
//         .then(data => {
//             console.log("Data received:", data);

//             // Process the received data and generate HTML table rows
//             let shipmentData = "";
//             for (let shipmentSno = 0; shipmentSno < data.length; shipmentSno++) {
//                 const v = data[shipmentSno];
//                 console.log("Processing data in loop");

//                 // Concatenate table row HTML with shipment data
//                 shipmentData += `<tr><td>${shipmentSno + 1}</td>
//             <td>${v.shipmentnumber}</td>
//             <td>${v.containerumber}</td>
//             <td>${v.routedetails}</td>
//             <td>${v.goodstype}</td>
//             <td>${v.device}</td>
//             <td>${v.expecteddeliverydate}</td>
//             <td>${v.ponumber}</td>
//             <td>${v.deliverynumber}</td>
//             <td>${v.ndcnumber}</td>
//             <td>${v.batchid}</td>
//             <td>${v.serialnumberofgoods}</td></tr>`;


//             }

//             // Update the content of the HTML table body with the constructed shipmentData
//             document.getElementById("table-body").innerHTML = shipmentData;

//             console.log("Data processing complete");
//         })
//         .catch(error => {
//             console.error("Error fetching or processing data:", error);
//         });
// });

if (localStorage.getItem("token") === null) {
    window.location.href = "/login";
}

$(document).ready(function () {
    const token = localStorage.getItem("token");



    console.log("Token:", token);

    // Check if token exists and not expired

    fetch(`/myshipmentData`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
            'Content-Type': 'application/json',
        }
    })
        .then(response => {
            console.log("Response Status:", response.status);

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

            let shipmentData = "";
            for (let shipmentSno = 0; shipmentSno < response.length; shipmentSno++) {
                const shipmentSno = response[shipmentSno];

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

            console.log("Shipment Data:", shipmentData);
            document.getElementById("table-body").innerHTML = shipmentData;
        })
        .catch(error => {
            console.log("Error:", error.message);
            // Check if the error is due to token expiration

        });

});