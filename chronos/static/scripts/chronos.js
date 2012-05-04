$(document).ready(function(){
	$("#sidebar li").draggable({
		revert: true,
		cursor: 'move',
		appendTo: 'body',
        helper: 'clone'
	});

	$("#main-content #month td").droppable({
		accept: ".support, .not_support",
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			// AJAX assignment creation and display should go here
			$( this )
				.addClass( "ui-state-highlight" )
				.find( ".assignments" )
					.append(event.srcElement);
			var date = $(this).attr('data-id');
			var person = $(event.srcElement).attr('data-id');
			$('#id_date').attr('value', date);
			$('#id_person').attr('value', person);
			$('#assignment-form').submit();
		}
	});

	$(".assignment").droppable({
		accept: ".role",
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			// AJAX role assignment and display update should go here
			$( this )
				.append(event.srcElement);
			var assignment = $(this).attr('data-id');
			var role = ui.draggable.data('id');

			$.post(
				'/assign-role/' + assignment + '/' + role + '/',
				{

				})
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
				},
				'json'
			);
		$(this).parent().remove();
		event.preventDefault();
	}
	);

	$( "#accordion" ).accordion({ active: 1 });

});