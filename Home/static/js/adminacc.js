if (sessionStorage.getItem("role") === "User") {
    window.location.href = "/login";
}

if (localStorage.getItem("token") === null) {
    window.location.href = "/login";
}

(function () {
    $(function () {
        var collapseMyMenu, expandMyMenu, hideMenuTexts, showMenuTexts;
        expandMyMenu = function () {
            return $("nav.sidebar").removeClass("sidebar-menu-collapsed").addClass("sidebar-menu-expanded");
        };
        collapseMyMenu = function () {
            return $("nav.sidebar").removeClass("sidebar-menu-expanded").addClass("sidebar-menu-collapsed");
        };
        showMenuTexts = function () {
            return $("nav.sidebar ul a span.expanded-element").show();
        };
        hideMenuTexts = function () {
            return $("nav.sidebar ul a span.expanded-element").hide();
        };
        return $("#justify-icon").click(function (e) {
            if ($(this).parent("nav.sidebar").hasClass("sidebar-menu-collapsed")) {
                expandMyMenu();
                showMenuTexts();
                $(this).css({
                    color: "#000"
                });
            } else if ($(this).parent("nav.sidebar").hasClass("sidebar-menu-expanded")) {
                collapseMyMenu();
                hideMenuTexts();
                $(this).css({
                    color: "#FFF"
                });
            }
            return false;
        });
    });

}).call(this);
////////////////////////////////////////////////////////////////////// 




$(document).ready(function () {
    // console.log("working");
    $("#username").text(` ${sessionStorage.getItem("username")}`);
    $("#email").text(`Email: ${sessionStorage.getItem("email")}`);
    $("#role").text(`Role    : ${sessionStorage.getItem("role")}`);
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