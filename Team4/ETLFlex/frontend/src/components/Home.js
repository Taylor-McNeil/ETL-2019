import React, {Component, Fragment} from 'react';
import { Link } from 'react-router-dom';
import Header from "./layout/Header";

export class Home extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <div className="card card-body pl-4 pr-4 mt-4">
                        <table className="table table-striped">
                            <thead>
                                <tr className="row">
                                    <th className="col-2">File ID</th>
                                    <th className="col-4">File Name</th>
                                    <th className="col-4">Last Upload</th>
                                    <th className="col-2"/>
                                </tr>
                            </thead>
                            {/* Comment: The loop goes down below in the <tbody>. */}
                            <tbody>
                                <tr className="row">
                                    <td className="col-2">1</td>
                                    <td className="col-4">f1.txt</td>
                                    <td className="col-4">11-15-2019</td>
                                    {/* Link 'edit' to History page */}
                                    <td className="col-2"><Link to="/filehistory">Edit</Link></td>
                                </tr>
                            </tbody>
                        </table>   
                    </div> 
                </div>
            </Fragment>
        )
    }
}

export default Home
