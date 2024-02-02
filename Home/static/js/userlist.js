if (localStorage.getItem("token") === null) {
    window.location.href = "/login";
}
document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        const token = localStorage.getItem("token");

        $("#submit").on("click", function (event) {
            event.preventDefault();
            const selectusername = $("#username").val();

            fetch("/userlist", {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "username": selectusername
                }),
            })
                .then(response => {
                    console.log(response);
                    if (response.status !== 200) {
                        throw new Error(`No User found`);
                    }else {
                        return response.json();
                    }
                    
                })
                .then(response => {
                    console.log(response);
                    let usersHTML = "";

                    for (let user_no = 0; user_no < response.data.length; user_no++) {
                        const user = response.data[user_no];

                        usersHTML += `<tr>
                            <td><input type="checkbox" class="user-checkbox"></td>
                            <td class="username">${user.username}</td>
                            <td>${user.email}</td>
                        </tr>`;
                    }

                    $("#tablebody").html(usersHTML);
                })
                .catch(error => {
                    console.log(error);
                    $("#successMessage").text("No User found");
                });
        });


        $("#tablebody").on("change", "input[type='checkbox']", function () {
            const selectedUsernames = [];


            $("input[type='checkbox']:checked").each(function () {
                const username = $(this).closest("tr").find(".username").text();
                selectedUsernames.push(username);
            });


            console.log("Selected Usernames:", selectedUsernames);
        });

        $("#makeAdmin").on("click", function (event) {
            event.preventDefault();

            const selectedUsernames = [];

            $("input[type='checkbox']:checked").each(function () {
                const username = $(this).closest("tr").find(".username").text().trim();
                if (username !== "") {
                    selectedUsernames.push(username);
                }
            });

            console.log("Selected Usernames:", selectedUsernames);

            if (selectedUsernames.length > 0) {
                fetch("/make_admin", {
                    method: "POST",
                    headers: {
                        "Authorization": `Bearer ${localStorage.getItem("token")}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ usernames: selectedUsernames }),
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`Status ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(response => {
                        console.log(response);

                        if (response.success) {
                            // Display success message
                            $("#successMessage").text(response.success.join("\n"));
                        } else if (response.error) {
                            // Display error message
                            $("#successMessage").text(response.error.join("\n"));
                        }
                    })
                    .catch(error => {
                        console.log("Error:", error.message);
                        // Display general error message
                        $("#successMessage").text(`Error: ${error.message}`);
                    });
            } else {
                // Display message when no users are selected
                $("#successMessage").text("No users selected");
            }
        });
       


    });
});