const user = JSON.parse(localStorage.getItem("user"));

if(user){

    document.getElementById("username").innerHTML =
        "Welcome " + user.full_name;

}else{

    window.location.href="login.html";

}