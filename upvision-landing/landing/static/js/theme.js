var icon = document.getElementById("icon");

icon.onclick = function () {
   document.body.classList.toggle("light-theme");
   if (document.body.classList.contains("light-theme")) {
      icon.src = "static/img/icons/moon.png";
   } else {
      icon.src = "static/img/icons/sun.png";
   }
}