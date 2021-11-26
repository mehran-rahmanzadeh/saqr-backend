
$(".sotial-media-nav").hover(function () {
    $(this).css("background-color", "white");
    $(this).children().css("color","black")
        
    }, function () {
        $(this).css("background-color", "transparent");
        $(this).children().css("color", "white");

    }
);

$(".manu-items").hover(function () {
    $(this).css("background-color", "transparent");
    $(this).children().css("color", "#8a1838");
    
    }, function () {
        $(this).children().css("color", "#000");
    }
);

$(".items-footer").hover(function() {
    $(this).children("svg").css("visibility","visible")
    $(this).children().css("color","#c41d4f")


}, function() {
    const hash=location.hash.replace("#","")
    const is_active=$(this).hasClass(hash);
    if(is_active){
       return 
    }
    $(this).children().css("color", "#FFF");
    $(this).children("svg").css("visibility", "hidden");

});

$(document).ready(function () {
    for(let a=0;a<=10;a++)
    {
        console.log(`#acc-detail${a}`)
        $(`#acc-detail${a}`).slideUp("fast");
    }
});
$(".accordion-head").click(function (e) { 
    e.preventDefault();
    $(this).children("i").toggleClass("transform180")
    let id=$(this).attr("data-num");
    $(`#acc-detail${id}`).slideToggle("fast");
    $(this).toggleClass("accordion-head--active");
    for(let a=0;a<=10;a++)
    {
        console.log(`#acc-detail${a}`)
        if(a!=id)
        {
            console.log(`#acc-detail${a}`)
            $(`#acc-detail${a}`).slideUp("fast");
            $(`#acc-head${a}`).removeClass('accordion-head--active');
            $(`#acc-head${a}`).children("i").removeClass("transform180")


        }
    }
});




$(document).ready(function () {
    $(".intro").children("svg").css("visibility","visible")
    $(".intro").children().css("color","#c41d4f")
});

$(window).on('hashchange', function (e) {

    if(location.hash=="#intro"){

        $(".intro").children("svg").css("visibility","visible")
        $(".intro").children().css("color","#c41d4f")
    }else{
        $(".intro").children().css("color", "#FFF");
        $(".intro").children("svg").css("visibility", "hidden");
    }

    if(location.hash=="#aboutus"){
        $(".aboutus").children("svg").css("visibility","visible")
        $(".aboutus").children().css("color","#c41d4f")
    }else{
        $(".aboutus").children().css("color", "#FFF");
        $(".aboutus").children("svg").css("visibility", "hidden");
    }

    if(location.hash=="#tracker"){
        $(".tracker").children("svg").css("visibility","visible")
        $(".tracker").children().css("color","#c41d4f")
    }else{
        $(".tracker").children().css("color", "#FFF");
        $(".tracker").children("svg").css("visibility", "hidden");
    }


    if(location.hash=="#dashboard"){
        $(".dashboard").children("svg").css("visibility","visible")
        $(".dashboard").children().css("color","#c41d4f")
    }else{
        $(".dashboard").children().css("color", "#FFF");
        $(".dashboard").children("svg").css("visibility", "hidden");
    }

    if(location.hash=="#blog"){
        $(".blog").children("svg").css("visibility","visible")
        $(".blog").children().css("color","#c41d4f")
    }else{
        $(".blog").children().css("color", "#FFF");
        $(".blog").children("svg").css("visibility", "hidden");
    }

    if(location.hash=="#quote"){
        $(".quote").children("svg").css("visibility","visible")
        $(".quote").children().css("color","#c41d4f")
    }else{
        $(".quote").children().css("color", "#FFF");
        $(".quote").children("svg").css("visibility", "hidden");
    }

    if(location.hash=="#footnote"){
        $(".footnote").children("svg").css("visibility","visible")
        $(".footnote").children().css("color","#c41d4f")
    }else{
        $(".footnote").children().css("color", "#FFF");
        $(".footnote").children("svg").css("visibility", "hidden");
    }
});


