
// direct browser to top right away
if (window.location.hash)
    scroll(0,0);
// takes care of some browsers issue
setTimeout(function(){scroll(0,0);},1);
if(window.location.hash){
// smooth scroll to the anchor id
$('html,body').animate({
    scrollTop:$(window.location.hash).offset().top - 70
    },1000,'swing');
}



function submitData(endPoint,formData,successMsg){
	var protocol    = location.protocol;
    var slashes     = protocol.concat("//");
    var host        = slashes.concat(window.location.hostname);
    host            += ":" + window.location.port;
	
	$.ajax({
		url: host + endPoint, 
        method:"POST",
        data:formData,
        success: function(resulte){
                    setSuccessMsg(successMsg);
                    openModal("confirmation-modal",null,"req-success");
        },
        error:function (err) {
        			console.log('erreur',err);
                    setErrMessage("une erreur inattendue s'est produite. veuillez réessayer ultérieurement");
                    openModal("confirmation-modal",null,"req-failed");
            }

	});
}







$(".news-letter-form").find('button').click(function (event) {
	event.preventDefault();
	let endPoint = $(this).attr('endpoint');
	let formData = $(this).parent().serialize();
	submitData(endPoint,formData,'vous etes maintenant inscrit à la newsletter');
	
});
$(".contact-form").find('button').click(function (event) {
	event.preventDefault();
	let endPoint = $(this).attr('endpoint');
	let formData = $(this).parent().parent().serialize();
	submitData(endPoint,formData,'Message envoyé');
});





$('.contact-trigger').click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top -70
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });

$('.services-carousel').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    mobileFirst: true,
    prevArrow: "<img class='a-left control-c prev slick-prev' src='/media/UI elements/SVGs/left-arrow.svg'>",
    nextArrow: "<img class='a-right control-c next slick-next' src='/media/UI elements/SVGs/right-arrow.svg'>",
    responsive: [
      {
        breakpoint: 998,
        settings: "unslick"
      },
      {
        breakpoint: 768,
        settings  : {slidesToShow: 3,
          slidesToScroll: 1}
      },

      {
        breakpoint: 560,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

$('.main-services-carousel').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    mobileFirst: true,
    prevArrow: "<img class='a-left control-c prev slick-prev' src='/media/UI elements/SVGs/left-arrow.svg'>",
    nextArrow: "<img class='a-right control-c next slick-next' src='/media/UI elements/SVGs/right-arrow.svg'>",
    responsive: [
      // {
      //   breakpoint: 1200,
      //   settings: "unslick"
      // },
      {
        breakpoint: 998,
        settings  : "unslick"
      },

      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

$('.travel-showcase-carousel').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    mobileFirst: true,
    prevArrow: "<img class='a-left control-c prev slick-prev' src='/media/UI elements/SVGs/left-arrow.svg'>",
    nextArrow: "<img class='a-right control-c next slick-next' src='/media/UI elements/SVGs/right-arrow.svg'>",
    responsive: [
      
      {
        breakpoint: 992,
        settings  : "unslick"
      },

      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

$('.testimonials-carousel').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    mobileFirst: true,
    prevArrow: "<img class='a-left control-c prev slick-prev' src='/media/UI elements/SVGs/left-arrow.svg'>",
    nextArrow: "<img class='a-right control-c next slick-next' src='/media/UI elements/SVGs/right-arrow.svg'>",
    responsive: [
      
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      },

      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });