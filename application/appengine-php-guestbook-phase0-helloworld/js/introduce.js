$(document).ready(function(){
	$('.name').click(function(){
		$('body').animate({'padding-top':"-=200px"},"slow");
	});
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
		$(".squirrel").css('left','50%');
		$(".squirrel").animate({'left':"-=30%"},"slow");
	});
	
	$('.E').click(function(){
		$('div>[class^="content"]').hide();
		$('.content-E').show();
	});
});
