import React, { Component } from 'react';

export class Landing extends Component {
    render() {
        return (
            <div className="vh-100 text-center">
                <div className="vh-100 jumbotron">
                    <h1 className="display-3">Welcome to F /_ E X</h1>
                    <p className="lead">James | Kamil | Frankie | Taylor</p>
                    <hr className="my-4" />
                        <p className="lead">
                            <a className="btn btn-primary btn-lg" href="http://127.0.0.1:8000/home" role="button">Login</a>
                        </p>
                </div>
            </div>
        )
    }
}

export default Landing
