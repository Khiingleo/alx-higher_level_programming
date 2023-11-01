$(function() {
    $('#btn_translate').click(function() {
        translateHello();
    });

    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            translateHello();
        }
    });

    function translateHello() {
        var languageCode = $('#language_code').val();
        var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;

        $.get(apiUrl, function(data) {
            $('#hello').text(data.hello);
        });
    }
});