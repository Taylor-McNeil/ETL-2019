import React from "react";
import Link from "next/link";

const Index = () => (
    <div>
        <h1>Suppose to be our landing :)</h1>
        <p>For now, just go to our login</p>
        <Link href="/login">
            <button type="button" className="btn btn-primary">Login</button>
        </Link>
    </div>
);

export default Index;
