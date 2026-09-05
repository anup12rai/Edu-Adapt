const form = document.getElementById("loginForm");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/api/auth/login",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            email:email,
            password:password
        })

    });

    const data = await response.json();

    if(data.success){

        alert("Login Successful");

        localStorage.setItem("user",JSON.stringify(data.user));

        window.location.href="dashboard.html";

    }else{

        alert(data.message);

    }

});