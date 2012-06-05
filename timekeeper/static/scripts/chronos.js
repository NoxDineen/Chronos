$(document).ready(function(){
	$("#sidebar li").draggable({
		revert: false,
		cursor: 'move',
		appendTo: 'body',
        helper: 'clone'
	});

	$("#main-content #month td").droppable({
		accept: ".support, .not_support",
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			$( this )
				// .addClass( "ui-state-highlight" )
				.find( ".assignments" )
					.append(event.srcElement);
			
			var date = $(this).attr('data-id');
			var person = $(event.srcElement).attr('data-id');
			if(ui.draggable.hasClass('support')) {
				var role = '1';
			}
			else {
				role = '1';
			}

			$('#id_date').attr('value', date);
			$('#id_person').attr('value', person);
			$('#id_role').attr('value', role);
			$('#assignment-form').submit();

			// This is what I need to use eventually, cheating with simple form submit for now to get things working
			// $.post('/', {
			// 	role: role,
			// 	date: date,
			// 	person: person
			// });
		}
	});

	$(".assignment").droppable({
		accept: ".role",
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			// $(this) is the <li> containing the assignment
			var mini_icon = ui.draggable.data('miniicon')
			$( this )
				.find('img').attr('src', mini_icon);
			var assignment = $(this).attr('data-id');
			var role = ui.draggable.data('id');
			$.post(
				'/assign-role/' + assignment + '/' + role + '/',
				{

				})
			event.preventDefault();
			}
	});

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

	$( "#accordion" ).accordion({ active: 1 });	// 1 is the Rockstars section, most commonly used by managers
  
	$( "#accordion2" ).accordion();	

	$('#add_close').click(function() {
		window.close();
	});

});
