$(function () {
    $("form").submit(function(){
        const uName = $("#username").val();
        const passwrd = $("#password").val();
        token = btoa(uName+":"+passwrd);
        localStorage.setItem("token", token)
    });
})