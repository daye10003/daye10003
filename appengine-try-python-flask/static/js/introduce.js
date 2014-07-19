$(document).ready(function(){
	// $('.name').click(function(){
	// 	$('body').animate({'padding-top':"-=200px"},"slow");
	// });
	// hide
	$('div>[class^="content"]').hide();

	$('.D').click(function(){
		$('div>[class^="content"]').hide();
		$('.content-D').show();
	});
	
	$('.A').click(function(){
		$('div>[class^="content"]').hide();
		$('.content-A').show();
	});
	
	$('.Y').click(function(){
		$('div>[class^="content"]').hide();
		$('.content-Y').show();
		$(".squirrel").css('left','65%');
		$(".squirrel").animate({'left':"-=27%"},"slow");
	});
	
	$('.E').click(function(){
		$('div>[class^="content"]').hide();
		$('.content-E').show();
	});
	$('.col-xs-1').hover(
		function(){
			$(this).addClass('active')
		},
		function(){
			$(this).removeClass('active')
		}
		);
	$("#rotating_moon").circulate({
	    speed: 600,                  // Speed of each quarter segment of animation, 1000 = 1 second
	    height: 160,                 // Distance vertically to travel
	    width: 360,                  // Distance horizontally to travel
	    sizeAdjustment: 150,         // Percentage to grow or shrink
	    loop: true,                 // Circulate continuously
	    zIndexValues: [-1, 1, 1, -1]   // Sets z-index value at each stop of animation
	});
});
