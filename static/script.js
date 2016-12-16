


$(document).ready(function() {
	introAnimation();
	emailSent();
	linkClick();
});


// navigation animation
$(window).scroll(function(){
	if ($(window).scrollTop() > 10)
		$('nav').css('box-shadow','0px 1px 4px lightgray');
	else
		$('nav').css('box-shadow','0px 0px 0px lightgray');
});


// link scroll animation
var linkClick = function(){
	$("nav a").click(function(e){
		e.preventDefault();
		var text = $(this).text();
		if (text == "Home"){
			$('html, body').animate({
		        scrollTop: 0
		    }, 1000);
		}
		else{
			$('html, body').animate({
		        scrollTop: $('a[name="' + text + '"]').offset().top - 60
		    }, 1000);
		}
	});
}


// scroll to email section if email was just sent
var emailSent = function(){
	if (document.getElementById('red').innerHTML != ""){
		$('html, body').animate({
	        scrollTop: $("#red").offset().top
	    }, 500);
	}
}



var introAnimation = function(){
	//var items = $("h2");
	var h = $("h2");


}
