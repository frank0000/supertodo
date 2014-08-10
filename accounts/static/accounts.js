/*global $ */

var initialize = function (navigator, user, token, urls) {
    $('#id_login').on('click', function () {
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            console.log('onlogin')
            $.post(
                urls.login,
                { assertion: assertion, csrfmiddlewaretoken: token }
            )
                .done(function () { console.log('DONE'); window.location.reload(); })
                .fail(function () { console.log('FAIL'); navigator.id.logout(); });
        },
        onlogout: function () {console.log('onlogout')}
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
