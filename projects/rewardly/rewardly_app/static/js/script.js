$(document).ready(function() {
    $('#id_email').keyup(function(){
        let emailInput = $(this).val();
        console.log('Email Entered: '+emailInput);

        // var data = $("#regForm").serialize() 
        var emailObject = {registrationEmail:emailInput}
        // console.log(data);
        $.ajax({
            method: "POST",   
            url: "/emailCheck",
            // data: {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, bodyData: JSON.stringify(emailObject)},
            data: JSON.stringify(emailObject),
            contentType: 'application/json',
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value}
        })
        .done(function(res){
            console.log(res);
            $('#emailMsg').html(res)
        })
    })

})
