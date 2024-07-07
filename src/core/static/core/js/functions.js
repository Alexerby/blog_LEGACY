// Main Header Scroll
$(function(){
    var lastScrollTop = 0, delta = 15;
    $(window).scroll(function(event){
       var st = $(this).scrollTop();
       
       if(Math.abs(lastScrollTop - st) <= delta)
          return;
if ((st > lastScrollTop) && (lastScrollTop>0)) {
       // downscroll 
      $("header").css("top","-200px");
  
   } else {
      // upscroll
      $("header").css("top","0px");
   }
       lastScrollTop = st;
    });
});

// Sidebar functionality
function showSidebar() {
    const sideBar = document.getElementById('sidebar') 
    sideBar.style.display = 'flex';
}

function hideSidebar() {
    const sideBar = document.getElementById('sidebar') 
    sideBar.style.display = 'none';
}

$(window).on('resize', function() {
    hideSidebar()
});


function toggleSidebar(elementId) {
  const targetElement = document.getElementById(elementId);
  if (window.getComputedStyle(targetElement).display === 'none') {
    targetElement.style.display = 'block'; 
  } else {
    targetElement.style.display = 'none';
  }
}
