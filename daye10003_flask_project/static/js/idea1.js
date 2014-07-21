$(document).ready(function(){
	$('[class^=ant]').hide();
	var count = 0;
	$('.super_ant').click(function(){
		count += 1;
		if(count<4){
			$('.ant'+count).show()
		}
		else{
			$('[class^=ant]').hide();
			// $(".super_ant_div").({left'250px'});
		}
	});
});