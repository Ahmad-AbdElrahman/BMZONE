document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.getElementById('navbar');
  
    navbar.addEventListener('click', function(event) {
      // Check if the clicked element is a link within the navbar
      if (event.target.tagName.toLowerCase() === 'a' && event.target.parentNode === navbar) {
        // Remove active class from all links
        const links = navbar.querySelectorAll('.nav-link');
        links.forEach(link => link.classList.remove('active'));
  
        // Add active class to the clicked link
        event.target.classList.add('active');
      }
    });
  });

var mainimg = document.getElementById("mainimg");
var smallimg = document.getElementsByClassName("small-img");

smallimg[0].onclick = function(){
    mainimg.src = smallimg[0].src;        
}
smallimg[1].onclick = function(){
    mainimg.src = smallimg[1].src;        
}
smallimg[2].onclick = function(){
    mainimg.src = smallimg[2].src;        
}
smallimg[3].onclick = function(){
    mainimg.src = smallimg[3].src;        
}

