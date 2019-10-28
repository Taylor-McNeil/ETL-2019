import React, { Component } from 'react';
import { Link } from 'react-router-dom'
export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <Link to="/" className="navbar-brand">F /_ E X</Link>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"/>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item active">
                            <Link to="/rules" className="nav-link">Create New Rule</Link>
                        </li>
                        <li className="nav-item float-sm-right">
                            <a className="nav-link">Logout</a>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }
}

export default Header
