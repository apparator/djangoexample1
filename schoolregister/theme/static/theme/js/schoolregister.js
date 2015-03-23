$( document ).ready(function() {

    $("#increase_passed_exams_button").click(function (event){
        event.preventDefault();
        $.ajax({
            method: "POST",
            url: "/students/1/increase_exams",
            data: { name: "John", location: "Boston" }
        })
        .done(function(data) {
            var number_of_passed_exams = data['passed_exams'];
            $("#passed_exams_cell").html(number_of_passed_exams);
        });        
    });

});