// back to top
//Get the button:
mybutton = document.getElementById("myBtn");
menu = document.getElementById('dp_menu')
img = document.getElementById('img')

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }

  if (document.body.scrollTop > 110 || document.documentElement.scrollTop > 110) {
	menu.style.display = 'block'
  $('.small-img').addClass(('fadeInLeft animated'))
  $('.title').addClass(('fadeIn animated'))
	} else {
	menu.style.display = 'none'
	}
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// hidden menu
$(document).ready(function(){
	$("button").click(function(){
		$("#dp_menu > ul").toggle(500);
		$("#dp_menu").toggleClass("show");
	});
});

// animate.css 
