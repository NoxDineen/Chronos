$(document).ready(function(){
	$("#sidebar li").draggable({
		revert: true,
		cursor: 'move',
		appendTo: 'body',
        helper: 'clone'
	});

	$("#main-content #month td").droppable({
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			// AJAX assignment creation and display should go here
			$( this )
				.addClass( "ui-state-highlight" )
				.find( ".assignments" )
					.append(event.srcElement);
			date = $(this).attr('data-id');
			person = $(event.srcElement).attr('data-id');
			$('#id_date').attr('value', date);
			$('#id_person').attr('value', person);
			$('#assignment-form').submit();
		}
	});


// Assignment deletion AJAXification
	$('.delete-assignment').submit(
		function( event ) {
			var assignment = $(this).parent().data('id');
			$.post(
				'/delete-assignment/' + assignment + '/',
				$(this).serializeArray(),
				function( data ) {
					console.log(data);
					$(this).parent.remove();
				},
				'json'
			);
		event.preventDefault();
	}
	);

	$( "#accordion" ).accordion();

});