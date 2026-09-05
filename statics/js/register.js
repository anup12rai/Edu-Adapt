const form = document.getElementById("registerForm");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const full_name = document.getElementById("full_name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/api/auth/register",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            full_name:full_name,
            email:email,
            password:password

        })

    });

    const data = await response.json();

    if(data.success){

        alert("Registration Successful");

        window.location.href="login.html";

    }else{

        alert(data.message);

    }

});