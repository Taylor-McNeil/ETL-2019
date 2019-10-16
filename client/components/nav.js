import React from 'react'
import Link from 'next/link'

const Nav = () => (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <Link href="/dashboard">
            <a className="navbar-brand" href="#">F /_ E X</a>
        </Link>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"/>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
                <li className="nav-item active">
                    <Link href="/data">
                        <a className="nav-link">Metadata <span className="sr-only">(current)</span></a>
                    </Link>
                </li>
                <li className="nav-item float-sm-right">
                    <Link href="http://127.0.0.1:8000/accounts/logout/">
                        <a className="nav-link">Logout</a>
                    </Link>
                </li>
            </ul>
        </div>
    </nav>
);

export default Nav



