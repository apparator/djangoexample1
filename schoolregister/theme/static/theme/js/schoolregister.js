

$(document).ready(function(){


    $("#increase_passed_exams_button").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: $('#passed_exams_url').val()
        })
        .done(function(data){
            var passed_exams_updated = data['passed_exams_updated'];
            $("#passed_exams_cell").html(passed_exams_updated);
        });
    });






});

