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
				},
				'json'
			);
		$(this).parent().remove();
		event.preventDefault();
	}
	);

	$( "#accordion" ).accordion({ active: 2 });

	function runToggle() {
			// get effect type from 
			var selectedEffect = blind;
			
			// most effect types need no options passed by default
			var options = {};
			// some effects have required parameters
			if ( selectedEffect === "scale" ) {
				options = { percent: 0 };
			} else if ( selectedEffect === "size" ) {
				options = { to: { width: 200, height: 60 } };
			}
			
			// run the effect
			$( "#role_icons" ).toggle( selectedEffect, options, 500 );
		};
		
		// set effect from select menu value
		$( "#roles" ).click(function() {
			runEffect();
			return false;
		});

});