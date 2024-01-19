if (localStorage.getItem("token") === null) {
  window.location.href = "/login";
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submit").addEventListener("click", function(event) {
      event.preventDefault();
        console.log("Dom load", localStorage.getItem("token"));
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
                "expected_delivery_date":$("#expected_delivery_date").val(),
                "po_num": $("#po_num").val(),
                "delivery_num": $("#delivery_num").val(),
                "ndc_num": $("#ndc_num").val(),
                "batch_id": $("#batch_id").val(),
                "serial_num": $("#serial_num").val(),
                "description": $("#description").val(),
             
            }),
            
             
          })
              .then(response => {
                  if (response.status === 200) {
                      return response.json();
                  }
                  else {
                    $("#error-message").text("Please Enter the emplty fields");
                    $("#error-message").css("visibility", "visible");
                }
              })
              .catch(error => {
                $("#error-message").text(error.message);
                $("#error-message").css("visibility", "visible");
            });
           
    });
});

