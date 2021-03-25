$(document).ready(function() {
    $('#cc_List').change(function() {
        var selected_option = $(this).val();
        $.ajax({
            url: <YOUR URL TO HANDLE THE REQUEST>+"/"+selected_option,
            type: 'post',
            cache: false,
            success: function(return_data) {
                $('#second_select').html(return_data);
            }
        });
    });


})
