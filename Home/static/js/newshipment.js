if (localStorage.getItem("token") === null) {
  window.location.href = "/login";
}

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("submit").addEventListener("click", function (event) {
    event.preventDefault();
    console.log("Dom load", localStorage.getItem("token"));

    // Reset error message visibility
    $("#error-message").css("visibility", "hidden");

    // Check if any field is empty
    const fields = ["shipment_num", "container_num", "route_details", "goods_type", "device", "expected_delivery_date", "po_num", "delivery_num", "ndc_num", "batch_id", "serial_num", "description"];

    for (const field of fields) {
      if ($("#" + field).val() === "") {
        $("#error-message").text("Please enter all fields");
        $("#error-message").css("visibility", "visible");
        return;
      }
    }
    const name=sessionStorage.getItem("username")
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
      .then(response => {
        console.log(response)
        if (response.status === 200) {
          // Clear form fields
          document.getElementById("myForm").reset();
          return response.json();
        } else {
          $("#error-message").text("Unexpected error");
          $("#error-message").css("visibility", "visible");
        }
      })
      .catch(error => {
        $("#error-message").text(error.message);
        $("#error-message").css("visibility", "visible");
      });
  });
});
