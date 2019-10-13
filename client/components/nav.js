import React from 'react'
import Link from 'next/link'
import "../style.css"

const Nav = () => (
    <header className='header'>
        <div className='wrap'>
            <nav className="nav-primary">
                <div className="wrap">
                    <ul className="genesis-nav-menu">
                        <li className="menu-item">
                            <Link href="/dashboard">
                                <a><span className="test">Home</span></a>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link href="/data">
                                <a><span className="test">Data</span></a>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link href="#">
                                <a><span className="test">Query</span></a>
                            </Link>
                        </li>
                    </ul>
                </div>
            </nav>
            <div className="title-area">
                <h1 className="site-title">
                    <Link href="/dashboard">
                        <a>F /_ e x</a>
                    </Link>
                </h1>
            </div>
            <nav className="nav-secondary">
                <div className="wrap">
                    <ul className="genesis-nav-menu">
                        <li className="menu-item">
                            <Link href="/dashboard">
                                <a><span className="test">Analysis</span></a>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link href="#">
                                <a><span className="test">Connect</span></a>
                            </Link>
                        </li>
                        <li className="menu-item">
                            <Link href="http://127.0.0.1:8000/accounts/logout/">
                                <a><span className="test">Logout</span></a>
                            </Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    </header>
);

export default Nav



