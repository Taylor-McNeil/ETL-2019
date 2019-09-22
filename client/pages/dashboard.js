import React from 'react';
import Layout from "../components/layout";
import Link from "next/link";

const Dashboard = () => (
    <div>
        <Layout/>
        <h1>Once again... WELCOME!</h1>
        <p>Let's start by designing our layout :P</p>
        <ol>
            <li>Login</li>
            <li>Metadata</li>
            <li>Dashboard</li>
            <ul>
                <li>Header</li>
                <li>Side Nav</li>
            </ul>
        </ol>
        <Link href="/">
            <button type="button" className="btn btn-primary">Go back home to repeat that fun little journey again :)</button>
        </Link>
    </div>
);

export default Dashboard;
