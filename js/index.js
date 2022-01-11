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
	}
  else {
    menu.style.display = 'none'
    }

  if (document.body.scrollTop > 1100 || document.documentElement.scrollTop > 1100){
    $('.title-teamName').addClass('fadeIn animated')
  }

  if (document.body.scrollTop > 1300 || document.documentElement.scrollTop > 1300){
    $('.text-teamName').addClass('fadeIn animated')
  }

  if (document.body.scrollTop > 1700 || document.documentElement.scrollTop > 1700){
    $('.title-personalInformation').addClass('fadeIn animated')
  }

  if (document.body.scrollTop > 3500 || document.documentElement.scrollTop > 3500){
    $('.title-projectDescription').addClass('fadeIn animated')
  }

  if (document.body.scrollTop > 3700 || document.documentElement.scrollTop > 3700){
    $('.topic').addClass('fadeInLeft animated')
    $('.topic-text').addClass('fadeInLeft animated')
  }

  if (document.body.scrollTop > 4500 || document.documentElement.scrollTop > 4500){
    $('.motivation').addClass('fadeInRight animated')
    $('.motivation-text').addClass('fadeInRight animated')
  }

  if (document.body.scrollTop > 4800 || document.documentElement.scrollTop > 4800){
    $('.landscape').addClass('fadeInUp animated')
    $('.landscape-text').addClass('fadeInUp animated')
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
