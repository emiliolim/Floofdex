import React from "react";
import "./css/loginForm.css"
const LoginForm = () => {
    return(
        <div>
            <div className={"form__signin"}>
                <h2 className={"sprompt"} >Sign Up</h2>
                <form>
                    <label className={"fname"}>First Name</label><br/>
                    <input type={"text"} className={"fname"}/><br/>
                    <label className={"email"}>Email</label><br/>
                    <input type={"email"} className={"email"}/><br/>
                    <label className={"password"}>Password</label><br/>
                    <input type={"password"} className={"password"}/><br/>
                    <input type={"submit"} className={"form__submit"}/>
                </form>
            </div>
        </div>
    );
}

export default LoginForm;