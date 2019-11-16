import React, { Component, Fragment } from 'react'
import Header from './layout/Header';

export class FileView extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <div className="card card-body pl-4 pr-4 mt-4">
                        <table className="table table-striped">
                            <thead>
                                <tr className="row">
                                    <th>Populate this based on # of columns</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr className="row">
                                    <td>Populate rows with get</td>
                                </tr>
                            </tbody>
                        </table>   
                    </div> 
                </div>
            </Fragment>
        )
    }
}

export default FileView
