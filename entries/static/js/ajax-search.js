$(document).ready(function() {

    $('#search').on('keyup',function () {

        $.ajax( {

            type: "POST",
            url: "/entry_search/",
            data: {
                    'text_search' : $('#search').val(),
                    csrfmiddlewaretoken: $('#csrftoken').val()
            }, 
            success: function SearchSuccess(data, textStatus, jqXHR) {
                     $('#search_results').html(data); 
            },   
            dataType: 'html' 
        });
    });
});

