if (localStorage.getItem("token") === null) {
  window.location.href = "/login";
}
function getFormattedDate() {
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, '0');
  const day = String(today.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

// Set the min attribute of the date input to today's date
document.getElementById('expected_delivery_date').min = getFormattedDate();

document.addEventListener("DOMContentLoaded", function () {

  document.getElementById("submit").addEventListener("click", function (event) {
    event.preventDefault();

    // Reset error message visibility
    $("#error-message").css("visibility", "hidden");

    // Check if any field is empty
    const fields = ["shipment_num", "container_num", "route_details", "goods_type", "device", "expected_delivery_date", "po_num", "delivery_num", "ndc_num", "batch_id", "serial_num", "description"];

    for (const field of fields) {
      if ($("#" + field).val() === "") {
        $("#error-message").text("Please enter all fields !!");
        $("#error-message").css({
          visibility: "visible",
          color: "white"
        });
        return;
      }
    }

    // If all fields are filled, proceed with the fetch
    fetch("/newshipment", {
      method: "POST",
      headers: {
        'Authorization': `Bearer ${localStorage.getItem("token")}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "shipment_num": $("#shipment_num").val(),
        "container_num": $("#container_num").val(),
        "route_details": $("#route_details").val(),
        "goods_type": $("#goods_type").val(),
        "device": $("#device").val(),
        "expected_delivery_date": $("#expected_delivery_date").val(),
        "po_num": $("#po_num").val(),
        "delivery_num": $("#delivery_num").val(),
        "ndc_num": $("#ndc_num").val(),
        "batch_id": $("#batch_id").val(),
        "serial_num": $("#serial_num").val(),
        "description": $("#description").val(),
      }),
    })
      .then(response => response.json().then(data => ({ status: response.status, body: data })))
      .then(data => {
        if (data.status === 200) {
          // Clear form fields
          document.getElementById("myForm").reset();

          // Display success message
          $("#error-message").text("Your Shipment has been done !");
          $("#error-message").css({
            visibility: "visible",
            color: "white"
          });

          // You may want to redirect or perform other actions here
        } else if (data.status === 400) {
          // Display the error message from the server
          $("#error-message").text(data.body.detail);
          $("#error-message").css({
            visibility: "visible",
            color: "white"
          });
        }
      })
      .catch(error => {
        console.error("Error:", error);
        $("#error-message").text("An error occurred.");
        $("#error-message").css("visibility", "visible");
      });
  });
});

