$(document).ready(function(){
	var p = new Pusher('5722854db044eae6e0f1');
	var channel = p.subscribe('syg');
	channel.bind('notification', function(data){
		alert(data.username+ " " + "is OnLine");});

	$('#button').click(function(){
		var text = $('#text').val();
		$.ajax({
			url : '/chatting',
			type : 'POST',
			data : {"text" : text},
			error : function(){
				console.log('error');
			},
			complete : function(){
				console.log('complete')
			},
		});
	})
	channel.bind('chatting', function(data){
		$('#daye').append('<p>'+data+'</p>')
	});
}); 