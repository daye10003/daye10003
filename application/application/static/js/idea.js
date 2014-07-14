$(document).ready(function(){
	$('[class^=idea]').hover(function(){
		$(this).addClass("active")
	},
	function(){
		$(this).removeClass('active')
	});
});
