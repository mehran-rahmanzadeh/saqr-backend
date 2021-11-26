let tracker=$("#tracker").offset();
let dashboard=$("#dashboard").offset();
let blog=$("#blog").offset();
let contactus=$("#contactus").offset();
let footnote=$("#footnote").offset();
let intro=$("#intro").offset();
let aboutus=$("#aboutus").offset();


$(window).scroll(function(){
    let scrollValue=$(window).scrollTop()

    if(scrollValue>0 && scrollValue<880)
    {   
        location.hash = "intro";
    }

    
    if(scrollValue>870 && scrollValue<1312)
    {   
        location.hash = "aboutus";
    }

    if(scrollValue>1305 && scrollValue<1750)
    {   
        location.hash = "tracker";
    }
    
    if(scrollValue>1740 && scrollValue<2625)
    {   
        location.hash = "dashboard";
    }
    
    if(scrollValue>2610 && scrollValue<3062)
    {   
        location.hash = "blog";
    }

    if(scrollValue>3042 && scrollValue<3500)
    {   
        location.hash = "quote";
    }

    if(scrollValue>3450 )
    {   
        location.hash = "footnote";
    }
});


