

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

    $(".points_link").click(function(event) {
        event.preventDefault();
        var note_id = $(this).data("noteid");
        var points_elm_id = "#id-points-" + note_id;

        $.ajax({
            url: $('#add_points_url').val() + "/" + note_id
        })
        .done(function(data){
            var points_updated = data['points_updated'];
            $(points_elm_id).html(points_updated);
        });

    });

});

