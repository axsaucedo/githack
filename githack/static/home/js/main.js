
function isScrolledIntoView(elem) { //returns true if an element is visible on screen

    var docViewTop = $(window).scrollTop(),
        docViewBottom = docViewTop + $(window).height(),
        elemTop = $(elem).offset().top,
        elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}

function scaleUpDown(elem, delay) { //scales an element up and down
    $(elem).addClass("scaleUp")
    setTimeout(function() {
       /* alert("la")*/
        $(elem).removeClass("scaleUp")
    }, delay)
}

var popDelay = 500, //delay between the pops of the 3 blocks
    scaleDelay = 500 //how long an element stays scaled up


$(function() {

    $("#header, #gh-matrix").addClass("ready") //animate GitHack header
    
    function onScroll() {
        
        if(/*isScrolledIntoView("#blured-divs") && */$("#blured-divs").hasClass("not-unblured")) { //if the 3 blocks are on the screen
            
            $("#blured-divs").removeClass("not-unblured")
            //scale up the 1st
            $("#blur1").addClass("unblur")
            scaleUpDown("#blur1", scaleDelay)
            //scale up the 2nd
            setTimeout(function(){
                $("#blur2").addClass("unblur")
                scaleUpDown("#blur2", scaleDelay)
            }, popDelay)
            //scale up the 3rd
             setTimeout(function(){
                $("#blur3").addClass("unblur")
                 scaleUpDown("#blur3", scaleDelay)
            }, popDelay*2)      
        }
        //unblur video
        if(isScrolledIntoView("#blur4")) {
              $("#blur4").addClass("unblur")
        }
    }
    
    $(window).scroll(onScroll);
})()