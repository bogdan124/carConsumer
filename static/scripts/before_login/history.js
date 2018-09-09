
function start_history_api(class_name,load_history){
	jQuery('document').ready(function(){
			 
			jQuery(class_name).on('click', function(e){
				e.preventDefault();
				var href = $(this).attr('href');
				 
				// Getting Content
				getContent(href, true);
				 
				jQuery(class_name).removeClass('active');
				$(this).addClass('active');
			});
			 
		});
		 
		// Adding popstate event listener to handle browser back button  
		window.addEventListener("popstate", function(e) {
			 
			// Get State value using e.state
			getContent(location.pathname, false,load_history);
		});
	}
     
    function getContent(url, addEntry,load_history) {
        $.get(url).done(function( data ) {
             
            // Updating Content on Page
            $(load_history).html(data);
             
            if(addEntry == true) {
                // Add History Entry using pushState
                history.pushState(null, null, url); 
            }
             
        });
    }
	
	
	function load_content_on_the_page(class_where_you_want_to_load_the_content,url_name){
		
		$(class_where_you_want_to_load_the_content).load(url_name);
		
		return false;
		
	}