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

			if(ui.draggable.hasClass('support')) {
				var role = '7';
			}
			else {
				role = '3';
			}
			$('#id_date').attr('value', date);
			$('#id_person').attr('value', person);
			$('#id_role').attr('value', role);
			$('#assignment-form').submit();
			event.preventDefault();
		}
	}
	);

	$(".assignment").droppable({
		accept: ".role",
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			// AJAX role assignment and display update should go here
			// $(this) is the <li> containing the assignment
			var mini_icon = ui.draggable.data('miniicon')
			$( this )
				.find('img').attr('src', mini_icon);
				//.replaceWith('miniicon');
			var assignment = $(this).attr('data-id');
			var role = ui.draggable.data('id');
			$.post(
				'/assign-role/' + assignment + '/' + role + '/',
				{

				})
			event.preventDefault();
			}
	}
	);

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