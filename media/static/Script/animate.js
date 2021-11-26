$(document).ready(function () {
    $(".login-menu-list").fadeOut(1);
    $(".loginmenudownicon").fadeOut(1);
    
    
    $(".lang-menu-list").fadeOut(1);
    $(".langmenudownicon").fadeOut(1);


    setTimeout(() => {
        $(".intro-image-background").removeClass("v-none");
        $(".intro-image-background").addClass("animate__animated animate__fadeIn");
    }, 800);
    setTimeout(() => {
        $(".saqr-main-text").removeClass("v-none");
        $(".saqr-main-line").removeClass("v-none");
        $(".saqr-main-svg").removeClass("v-none");

        $(".saqr-main-text").addClass("animate__animated animate__fadeIn");
        $(".saqr-main-line").addClass("animate__animated animate__fadeIn");
        $(".saqr-main-svg").addClass("animate__animated animate__fadeIn");

    }, 300);
});


$(".auth-dropdown").click(function (e) { 
    e.preventDefault();
    $(".login-menu-list").fadeToggle('fast');
    $(".loginmenudownicon").fadeToggle('fast');

});

$(".lang-dropdown").click(function (e) { 
    e.preventDefault();
    $(".lang-menu-list").fadeToggle('fast');
    $(".langmenudownicon").fadeToggle('fast');

});

$(".lang-dropdown").click(function (e) { 
    e.preventDefault();


});



$(window).click(function (e) { 
    e.preventDefault();
    if(e.target.className!="auth-dropdown" && e.target.className!="fas fa-chevron-down" && e.target.id!="login-text-svg" && e.target.id!="login-text-btn" ){
        $(".login-menu-list").fadeOut('fast');
        $(".loginmenudownicon").fadeOut('fast');

    }

    if(e.target.className!="lang-dropdown" && e.target.className!="fas fa-chevron-down a" && e.target.id!="lang-text-svg" && e.target.id!="lang-text-btn" ){
        $(".lang-menu-list").fadeOut('fast');
        $(".langmenudownicon").fadeOut('fast');

    }

});

$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    console.log(scrollValue)
    if(scrollValue>400)
    {   
        setTimeout(() => {
            $('#sec2-h3-1').removeClass('v-none');
            $('#sec2-h3-1').addClass("animate__fadeIn ");
            //sec2-p-1
        }, 250);
        setTimeout(() => {
            $('#sec2-p-1').removeClass('v-none');
            $('#sec2-p-1').addClass("animate__fadeIn");
            
        }, 600);

        setTimeout(() => {
            $('#sec2-h5-1').removeClass('v-none');
            $('.hawk-id-sec').removeClass('v-none');

            $('#sec2-h5-1').addClass("animate__fadeIn");
            $('.hawk-id-sec').addClass("animate__fadeIn");
            
        }, 1100);
        
        setTimeout(() => {
            $('.sec-section-image').removeClass('v-none');
            $('.sec-section-image').addClass("animate__fadeIn");
            
        }, 1400);

        setTimeout(() => {
            $('.hawk-image-description-1-div').removeClass('v-none');
            $('.hawk-image-description-1-div').addClass("animate__fadeIn");
            
        }, 1500);

        setTimeout(() => {
            $('.hawk-image-description-2-div').removeClass('v-none');
            $('.hawk-image-description-2-div').addClass("animate__fadeIn");
            
        }, 1700);

        setTimeout(() => {
            $('.hawk-image-description-3-div').removeClass('v-none');
            $('.hawk-image-description-3-div').addClass("animate__fadeIn");
            
        }, 1900);

        
       
    }
    
    
});

$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    console.log(scrollValue)
    if(scrollValue>800)
    {

        setTimeout(() => {
            $('.aboutus-img1').removeClass('v-none');
            $('.aboutus-img1').addClass('animate__fadeIn');    
        }, 200);

        setTimeout(() => {
            $('.aboutus-img2').removeClass('v-none');
            $('.aboutus-img2').addClass('animate__fadeIn');    
        }, 400);

        setTimeout(() => {
            $('#demo01').removeClass('v-none');
            $('#demo01').addClass('animate__fadeIn');    
        }, 600);

        setTimeout(() => {
            $('.sec3-h3').removeClass('v-none');
            $('.sec3-h3').addClass('animate__fadeIn');    
        }, 900);
        setTimeout(() => {
            $('.sec3-p').removeClass('v-none');
            $('.sec3-p').addClass('animate__fadeIn');    
        }, 1100);
    }   
        
    

});

$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    console.log(scrollValue)
    if(scrollValue>1200)
    {
        setTimeout(() => {
            $('#mozhol-image-main').removeClass('v-none');
            $('#mozhol-image-main').addClass('animate__fadeIn');    
        }, 200);

        setTimeout(() => {
            $('.tracker-h3').removeClass('v-none');
            $('.tracker-h3').addClass('animate__fadeIn');    
        }, 400);

        setTimeout(() => {
            $('.tracker-p').removeClass('v-none');
            $('.tracker-p').addClass('animate__fadeIn');    
        }, 600);

        setTimeout(() => {
            $('.tracker-svg').removeClass('v-none');
            $('.tracker-svg').addClass('animate__fadeIn');    
        }, 800);
    }   
        
    

});


$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    console.log(scrollValue)
    if(scrollValue>1600)
    {
        setTimeout(() => {
            $('.dashboard-svg').removeClass('v-none');
            $('.dashboard-svg').addClass('animate__fadeIn');    
        }, 200);

        setTimeout(() => {
            $('.dashboard-image-pos1').removeClass('v-none');
            $('.dashboard-image-pos1').addClass('animate__fadeIn');    
        }, 700);

        setTimeout(() => {
            $('.dashboard-image-pos2').removeClass('v-none');
            $('.dashboard-image-pos2').addClass('animate__fadeIn');    
        }, 1000);

        setTimeout(() => {
            $('.dashbaord-h3').removeClass('v-none');
            $('.dashbaord-h3').addClass('animate__fadeIn');    
        }, 1200);

        setTimeout(() => {
            $('.dashbaord-p').removeClass('v-none');
            $('.dashbaord-p').addClass('animate__fadeIn');    
        }, 1400);
    }   
});



$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    if(scrollValue>2000)
    {
        setTimeout(() => {
            $('.background-text').removeClass('v-none');
            $('.background-text').addClass('animate__fadeIn');    
        }, 200);

        setTimeout(() => {
            $('.imageCertificate').removeClass('v-none');
            $('.imageCertificate').addClass('animate__fadeIn');    
        }, 700);

        setTimeout(() => {
            $('.h3-sertificate').removeClass('v-none');
            $('.h3-sertificate').addClass('animate__fadeIn');    
        }, 900);


        setTimeout(() => {
            $('.p-sertificate').removeClass('v-none');
            $('.p-sertificate').addClass('animate__fadeIn');    
        }, 1100);

        setTimeout(() => {
            $('.h5-sertificate').removeClass('v-none');
            $('.h5-sertificate').addClass('animate__fadeIn');    
        }, 1300);

        setTimeout(() => {
            $('.inutclass').removeClass('v-none');
            $('.inutclass').addClass('animate__fadeIn');    
        }, 1500);

        
    }   
});

$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    if(scrollValue>2400)
    {
        setTimeout(() => {
            $('.postanimate1').removeClass('v-none');
            $('.postanimate1').addClass('animate__fadeIn');    
        }, 200);  
        
        setTimeout(() => {
            $('.postanimate2').removeClass('v-none');
            $('.postanimate2').addClass('animate__fadeIn');    
        }, 400);

        setTimeout(() => {
            $('.postanimate3').removeClass('v-none');
            $('.postanimate3').addClass('animate__fadeIn');    
        }, 600);

        setTimeout(() => {
            $('.postanimate4').removeClass('v-none');
            $('.postanimate4').addClass('animate__fadeIn');    
        }, 600);

        setTimeout(() => {
            $('.postanimate5').removeClass('v-none');
            $('.postanimate5').addClass('animate__fadeIn');    
        }, 600);
    }   
});


$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    if(scrollValue>2800)
    {
        setTimeout(() => {
            $('.contactus-h3').removeClass('v-none');
            $('.contactus-h3').addClass('animate__fadeIn');    
        }, 200);  

        setTimeout(() => {
            $('.contactus-p').removeClass('v-none');
            $('.contactus-p').addClass('animate__fadeIn');    
        }, 600);  

        setTimeout(() => {
            $('.Sotialmedia-diva').removeClass('v-none');
            $('.Sotialmedia-diva').addClass('animate__fadeIn');    
        }, 1000);

        setTimeout(() => {
            $('.contactus-sec-2').removeClass('v-none');
            $('.contactus-sec-2').addClass('animate__fadeIn');    
        }, 1300);


        setTimeout(() => {
            $('.name-textbox').removeClass('v-none');
            $('.name-textbox').addClass('animate__fadeIn');    
        }, 1500);

        setTimeout(() => {
            $('.name-email').removeClass('v-none');
            $('.name-email').addClass('animate__fadeIn');    
        }, 1700);

        setTimeout(() => {
            $('.name-subject').removeClass('v-none');
            $('.name-subject').addClass('animate__fadeIn');    
        }, 1900);

        setTimeout(() => {
            $('.name-phone').removeClass('v-none');
            $('.name-phone').addClass('animate__fadeIn');    
        }, 2100);

        setTimeout(() => {
            $('.name-description').removeClass('v-none');
            $('.name-description').addClass('animate__fadeIn');    
        }, 2300);

        setTimeout(() => {
            $('.btnanimate').removeClass('v-none');
            $('.btnanimate').addClass('animate__fadeIn');    
        }, 2500);

        
    }   
});



$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()
    if(scrollValue>3200)
    {
        setTimeout(() => {
            $('.faq-h3').removeClass('v-none');
            $('.faq-h3').addClass('animate__fadeIn');    
        }, 200);  

        setTimeout(() => {
            $('#acc-head1').removeClass('v-none');
            $('#acc-head1').addClass('animate__fadeIn');    
        }, 500);  

        setTimeout(() => {
            $('#acc-head2').removeClass('v-none');
            $('#acc-head2').addClass('animate__fadeIn');    
        }, 800);  

        setTimeout(() => {
            $('#acc-head3').removeClass('v-none');
            $('#acc-head3').addClass('animate__fadeIn');    
        }, 1100);  

        
    }   
});










