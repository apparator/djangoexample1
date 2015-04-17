

$(document).ready(function(){

    $(".add-points-link").click(function(event) {
        event.preventDefault();
        var note_id = $(this).data("noteid");
        $.ajax({
            url: $('#add_points_url').val() + "/" + note_id
        })
        .done(function(data){
            var points_updated = data['points_updated'];
            var points_element_id = "#id-points-for-note-" + note_id;
            $(points_element_id).html(points_updated);
        });
    });

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

