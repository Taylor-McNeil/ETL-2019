import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import Header from './layout/Header';

export class FileHistory extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <div className="card card-body pl-4 pr-4 mt-4">
                        <h3>Filename Here</h3>
                        <table className="table table-striped">
                            <thead>
                                <tr className="row">
                                    <th className="col-2">Date</th>
                                    <th className="col-4">Rows</th>
                                    <th className="col-2"></th>
                                </tr>
                            </thead>
                            {/* Comment: The loop goes down below in the <tbody>. */}
                            <tbody>
                                <tr className="row">
                                    <td className="col-2">11-15-2019</td>
                                    <td className="col-4">30</td>
                                    <th className="col-2"><Link to="/fileview">View</Link></th>
                                </tr>
                            </tbody>
                        </table>   
                    </div> 
                </div>
            </Fragment>
        )
    }
}

export default FileHistory
