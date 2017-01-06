$(document).ready(function(){

  $('.owl-carousel').owlCarousel({
    // rtl:true,
    loop:true,
    margin:10,
    // nav:true,
    center: true,
    autoplay:true,
    autoplayTimeout:4000,
    autoplayHoverPause:false,
    autoWidth:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
  });

});
