import React, {Component, Fragment} from 'react';
import Header from "./layout/Header";

export class Home extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container vh-100">
                    <div className="h-100 align-items-center align-middle">
                        <div className="text-center">
                            <h1 className="mt-5 mt-5 mt-5">Hewo</h1>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default Home
