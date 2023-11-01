$(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
        var movies = data.results;
        for (let i in movies) {
            $('#list_movies').append('<li>' + movies[i].title + '</li>');
        }
    });
});