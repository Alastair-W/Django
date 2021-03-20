$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault();
        $.ajax({
            url: 'favorite',
            method: 'post',
            data: /* Any data to send along? */,
            success: function(serverResponse){
                $('.favorite').html(serverResponse)
            }
        })
    })
})