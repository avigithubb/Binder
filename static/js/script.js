const swiper = new Swiper('.swiper', {

    a11y: {
        prevSlideMessage: 'Previous slide',
        nextSlideMessage: 'Next slide',
      },

    allowSlideNext: true,
    allowSlidePrev:true,
    allowTouchMove:true,
    autoHeight:true,
    autoplay: {
        delay: 5000,
      },

    slidesPerView: 1,
    spaceBetween: 10,
    // Responsive breakpoints
    breakpoints: {
        // when window width is >= 320px
        320: {
        slidesPerView: 2,
        spaceBetween: 20
        },
        // when window width is >= 480px
        480: {
        slidesPerView: 3,
        spaceBetween: 30
        },
        // when window width is >= 640px
        640: {
        slidesPerView: 4,
        spaceBetween: 40
        }
    },

    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    scrollbars:{
        removeEventListener:true,
    }
    // And if we need scrollbar
  });

  $(window).scroll(function()
  {
    $(".main-head").css("opacity", 1 - $(window).scrollTop() / 300);
  });

  $(window).scroll(function()
  {
    $(".acc").css("opacity", 1 - $(window).scrollTop() / 300);
  });

var prevScrollpos = window.pageYOffset;

    window.onscroll = function() {
        var currentScrollPos = window.pageYOffset;
        var navbar = document.getElementById("top-nav");

        if (prevScrollpos > currentScrollPos) {
            navbar.style.opacity = "1";
        } else {
            navbar.style.opacity = "0";
        }

        prevScrollpos = currentScrollPos;
    };
