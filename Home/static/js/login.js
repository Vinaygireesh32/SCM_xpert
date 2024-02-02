let captcha;
let alphabets = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz";
let status = document.getElementById('status');


function generate() {
    let first = alphabets[Math.floor(Math.random() * alphabets.length)];
    let second = Math.floor(Math.random() * 10);
    let third = Math.floor(Math.random() * 10);
    let fourth = alphabets[Math.floor(Math.random() * alphabets.length)];
    let fifth = alphabets[Math.floor(Math.random() * alphabets.length)];
    let sixth = Math.floor(Math.random() * 10);
    captcha = first.toString() + second.toString() + third.toString() + fourth.toString() + fifth.toString() + sixth.toString();
    document.getElementById('generated-captcha').value = captcha;
    document.getElementById("entered-captcha").value = '';
}

function validateForm() {
    let userValue = document.getElementById("entered-captcha").value;
    if (userValue.toLowerCase() === captcha.toLowerCase()) {
        return true;
    } else {
        status.innerText = "Try Again!";
        document.getElementById("entered-captcha").value = '';
        return false;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('submit').addEventListener('click', function (event) {
        // Prevent the default action (navigation to the specified URL)
        event.preventDefault();

        // Check if the captcha is entered correctly
        if (validateForm()) {
            // Now, you can add your custom logic
            console.log($("#username").val())
            console.log($("#password").val())
            const formData = new FormData();
            formData.append("username", $("#username").val());
            formData.append("password", $("#password").val());
            fetch("/login", {
                method: "POST",
                body: formData,
            })
               
                .then(response => {
                    if (response.status === 200) {
                        return response.json();
                    } else {
                        throw new Error("Invalid username or password");
                    }
                })
                .then(response => {
                    console.log(response);
                
                    localStorage.setItem("token", `${response.token}`);
                    sessionStorage.setItem("username", `${response.username}`);
                    sessionStorage.setItem("email", `${response.email}`);
                    sessionStorage.setItem("role", `${response.role}`);
                    if (localStorage.getItem("token") !== null && response.role === "User") {
                        window.location.href = "/dashboard";
                    } else {
                        window.location.href = "/admin";
                    }
                })
                .catch(error => {
                    $(".error-message").text(error.message); // Display the error message
                    $(".error-message").css("visibility", "visible");
                });
        } else {
            // Captcha validation failed, you can handle it here
            // For now, you may want to display an error message or take appropriate action
            console.log("Captcha validation failed");
        }
    });

    // Initial captcha generation on page load
    generate();
});


