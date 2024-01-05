(function() {
    $(function() {
      var collapseMyMenu, expandMyMenu, hideMenuTexts, showMenuTexts;
      expandMyMenu = function() {
        return $("nav.sidebar").removeClass("sidebar-menu-collapsed").addClass("sidebar-menu-expanded");
      };
      collapseMyMenu = function() {
        return $("nav.sidebar").removeClass("sidebar-menu-expanded").addClass("sidebar-menu-collapsed");
      };
      showMenuTexts = function() {
        return $("nav.sidebar ul a span.expanded-element").show();
      };
      hideMenuTexts = function() {
        return $("nav.sidebar ul a span.expanded-element").hide();
      };
      return $("#justify-icon").click(function(e) {
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
  // Store token in localStorage
localStorage.setItem('token', 'your_token_value');

// Retrieve token from localStorage
const storedToken = localStorage.getItem('token');

// // Open a database
// const db = indexedDB.open('myDatabase', 1);

// // Store token in the database
// db.onsuccess = function(event) {
//   const database = event.target.result;
//   const transaction = database.transaction(['tokens'], 'readwrite');
//   const objectStore = transaction.objectStore('tokens');
//   objectStore.add('your_token_value', 'token_key');
// };

// // Retrieve token from the database
// db.onsuccess = function(event) {
//   const database = event.target.result;
//   const transaction = database.transaction(['tokens']);
//   const objectStore = transaction.objectStore('tokens');
//   const request = objectStore.get('token_key');
//   request.onsuccess = function(event) {
//     const storedToken = event.target.result;
//   };
// };



  