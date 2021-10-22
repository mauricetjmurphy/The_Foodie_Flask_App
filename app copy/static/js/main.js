(function ($) {
    "use strict";

    /*=============================
	    Preloader
	=============================*/

    $(window).on("load", function () {
        $(".preloader").delay(200).fadeOut("slow");
    });

    /*=============================
	    Hero Slider
	============================*/

    $("#hero-slider").slick({
        infinite: true,

        arrows: true,

        dots: false,

        autoplay: true,

        responsive: [
            {
                breakpoint: 768,

                settings: {
                    dots: true,

                    arrows: false,
                },
            },
        ],
    });
})(jQuery);
