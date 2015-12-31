$(".addInTable").click(function () {
    var date = $(".date").val();
    var home = $(".home").val();
    var homegoals = $(".homegoals").val();
    var awaygoals = $(".awaygoals").val();
    var away = $(".away").val();
    var league = $(".league").val();
    $.ajax({
        type: "POST",
        url:  "upl/",
        data: { date: date , home : home , homegoals: homegoals, awaygoals: awaygoals, away: away , league: league },
        success: function () {
            window.location.reload();
        },
        error: function () {
            alert("ERROR !!");
        }
    })
});
