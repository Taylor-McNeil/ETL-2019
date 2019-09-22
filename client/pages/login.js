import React from 'react';
import Link from "next/link";

const Login = () => (
    <div>
        <h1>Login in pl0x</h1>
        <p>Welcome to the login! We too have not made this so...</p>
        <p>Go to the dashboard!</p>
        <Link href="/dashboard">
            <button type="button" className="btn btn-primary">Dashboard</button>
        </Link>
    </div>
);

export default Login;
