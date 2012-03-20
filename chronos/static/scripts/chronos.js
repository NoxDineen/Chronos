$(document).ready(function(){
	$("#sidebar li").draggable({revert: true});

	$("#main-content #month td").droppable({
		hoverClass: "ui-state-active",
		drop: function( event, ui ) {
			$( this )
				.addClass( "ui-state-highlight" )
				.find( "p" )
					.html( "Magic!" );
		}
	});

});