document.addEventListener('DOMContentLoaded', function(){
    var workout_option = document.getElementById("workout_option");
    workout_option.addEventListener("click", function(){
        window.location.href = "/create_workout";
    });

    var exercise_option = document.getElementById("exercise_option");
    exercise_option.addEventListener("click", function(){
        window.location.href = "/add/create_exercise";
    });
});
