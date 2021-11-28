$(".items-footer").on("click", function (event) {
    let scrollValue=$(window).scrollTop()
    console.log(scrollValue)
    event.preventDefault();
    var id = $(this).children('a').attr('href');
    switch (id) {
        case "#intro":
            $('body,html').animate({
                scrollTop: 0
            }, 1500);
            break;
        case "#aboutus":
            $('body,html').animate({
                scrollTop: 880
            }, 1500);
            break;
        case "#tracker":
            $('body,html').animate({
                scrollTop: 1310
            }, 1500);
            break;
        case "#dashboard":
            $('body,html').animate({
                scrollTop: 1750
            }, 1500);
            break;
        case "#blog":
            $('body,html').animate({
                scrollTop: 2620
            }, 1500);  
            break;
        case "#contactus":
            $('body,html').animate({
                scrollTop: 3052
            }, 1500);  
            break;
        case "#footnote":
            $('body,html').animate({
                scrollTop: 3500
            }, 1500);
            break;
            
    }

    
});






