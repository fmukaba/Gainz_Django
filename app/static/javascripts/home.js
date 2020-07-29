document.addEventListener('DOMContentLoaded', function() {
    var viewBtns = document.getElementsByClassName('viewBtn');
    for (let i = 0; i<viewBtns.length; i++){      
        viewBtns[i].addEventListener('click', function() {
            var id = viewBtns[i].id;
            var num = id.split("_")[1];
            window.location.href = "view_workout/"+num;
        });
    } 

    var completedBtns = document.getElementsByClassName('completedBtn');
    for (let i = 0; i<viewBtns.length; i++){      
        completedBtns[i].addEventListener('click', function() {
            var id = completedBtns[i].id;
            var num = id.split("_")[1];
            window.location.href = "completed/"+num;
        });
    }
})

