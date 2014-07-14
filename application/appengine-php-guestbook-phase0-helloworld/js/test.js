$(document).ready(function(){
	$('.carousel').carousel({
		interval: 2000
	});
	$('#right').tooltip('show');
	$('#hi').click(function(){
		$(this).fadeOut('slow');
	});
	$('#hi2').click(function(){
		$(this).detach();
	});
});