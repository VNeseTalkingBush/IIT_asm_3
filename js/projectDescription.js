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
        $('.detail-title').addClass('fadeIn animated')
    }
    else {
        menu.style.display = 'none'
    }

    if (document.body.scrollTop > 130 || document.documentElement.scrollTop > 130){
        $('.aim').addClass('fadeInLeft animated')
        $('.aim-text').addClass('fadeInLeft animated')
      }

    if (document.body.scrollTop > 530 || document.documentElement.scrollTop > 530)  {
      $('.goal').addClass('fadeInRight  animated')
      $('.row.goal').addClass('fadeInRight animated')
    }
    
    if (document.body.scrollTop > 2600 || document.documentElement.scrollTop > 2600){
        $('.planAndProgress').addClass('bounceIn animated')
      }

    if (document.body.scrollTop > 4000 || document.documentElement.scrollTop > 4000){
        $('.role').addClass('fadeInUp animated')
      }

    if (document.body.scrollTop > 4700 || document.documentElement.scrollTop > 4700){
        $('.scopeAndLimit').addClass('fadeInLeft animated')
      }

    if (document.body.scrollTop > 6500 || document.documentElement.scrollTop >6500){
        $('.toolAndTechnology').addClass('fadeInRight animated')
      }

    if (document.body.scrollTop > 7500 || document.documentElement.scrollTop > 7500){
        $('.testingAndTimeframe').addClass('fadeInUp animated')
      }

    if (document.body.scrollTop > 10000 || document.documentElement.scrollTop > 10000){
        $('.risk').addClass('fadeInDown animated')
      }

    if (document.body.scrollTop > 11500 || document.documentElement.scrollTop > 11500){
        $('.communication').addClass('fadeIn animated')
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