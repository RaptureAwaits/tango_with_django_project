var year_buttons = document.getElementsByClassName("year_button");
var i;

function expand_content(button_id) {
    content_id = 'ydiv' + button_id
    content_div = document.getElementById(content_id)

    if (content_div.style.display == "block") {
      content_div.style.display = "none";
    } else {
      content_div.style.display = "block";
    }
}