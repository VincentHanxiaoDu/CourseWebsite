$(document).ready(function () {
    var scene = "login";
    $(document).keypress(function (event) {
        if (event.keyCode === 13) {
            if (scene==="login") {
                $("#submit").click();
            }
            if (scene==="register") {
                $("#reg-submit").click();
            }
        }
    });

    /* get a parameter from url*/
    function get_param_val(param_name) {
        var url = document.location.toString();
        var array = url.split("?");
        if (array.length > 1) {
            var params = array[1].split("&");
            for (let i = 0; i < params.length; i++) {
                let param = params[i].split("=");
                if (param !== null && param[0] === param_name) {
                    return param[1];
                }
            }
            return "";
        }
        return "";
    }

    $("#register").click(function () {
        scene = "register";
        $("#login-frame").hide();
        let reg = $("#register-frame");
        reg.fadeIn(1000);
        reg.attr("style", "display: inline-block;");
    });

    $("#login").click(function () {
        scene = "login";
        $("#register-frame").hide();
        let log = $("#login-frame");
        log.fadeIn(1000);
        log.attr("style", "display: inline-block;");
    });

    $("#submit").click(function () {
        username = $("#username").val();
        password = $("#password").val();
        type = $("#type").val();

        /* login POST */
        $.post("/login", {
            'username': username,
            'password': password,
            'logintype': type
        }, function (result, code) {
            let status = result['status'];
            if (code === "success") {
                if (status === "True" && (redirect = get_param_val("request_url"))) {
                    window.location.href = (decodeURIComponent(redirect));
                } else if (status === "True") {
                    window.location.href = "/";
                } else {
                    alert(result['reason'] + ", please try again!");
                    $("#username").val("");
                    $("#password").val("");
                }
            } else {
                alert("Login failed, please try again!");
                window.location.reload();
            }
        });
    });

    $("#reg-submit").click(function () {
        username = $("#reg-username").val();
        password = $("#reg-password").val();
        firstname = $("#reg-firstname").val();
        lastname = $("#reg-lastname").val();
        type = $("#reg-type").val();
        /* Register POST */
        $.post("/register", {
            'username': username,
            'password': password,
            'firstname': firstname,
            'lastname': lastname,
            'regtype': type,
        }, function (result, code) {
            let status = result['status'];
            if (status === 'True') {
                
            }
        })
    });
});