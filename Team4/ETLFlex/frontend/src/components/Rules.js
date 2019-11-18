import React, {Component, Fragment} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getRules, deleteRules } from "../actions/rules";
import { Link } from 'react-router-dom';

import rules from "../reducers/rules";
import RulesForm from "./RulesForm";
import Header from "./layout/Header";

class Rules extends Component {
    /*
    static propTypes = {
        rules: PropTypes.array.isRequired,
        getRules: PropTypes.func.isRequired,
        deleteRules: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getRules();
    }
    */


    render () {
        return (
           <Fragment>
               <Header />
               {/*
               <div className="container">
                   <div className="card card-body p-4">
                       <RulesForm />
                       <h2>Rules</h2>
                       <table className="table table-striped">
                           <thead>
                           <tr className="row">
                               <th className="col-2">Column ID</th>
                               <th className="col-9">Column Header</th>
                               <th className="col-1"/>
                           </tr>
                           </thead>
                           <tbody>
                           { this.props.rules.map(rules => (
                               <tr className="row" key={rules.id}>
                                   <td className="col-2">{rules.col_num}</td>
                                   <td className="col-8">{rules.col_header}</td>
                                   <td className="col-2 text-right"><button onClick={this.props.deleteRules.bind(this, rules.id)} className="btn btn-outline-danger btn-sm">Delete</button></td>
                               </tr>
                           ))}
                           </tbody>
                       </table>
                   </div>
                   <div className="text-right mt-4">
                        <button className="btn btn-info text-right">
                            <Link to="/" className="text-white">Finish</Link>
                        </button>
                   </div>
               </div>
                */}
                <div className="container">
                    <div className="card card-body p-4 mt-4">
                        <form>
                            {/* Input for source */}
                            <div className="form-group">
                                <label>Data Source</label>
                                <input type="text" className="form-control" id="datasrc" placeholder="Enter an address or link" />
                                <small className="form-text text-muted">Enter the FTP address or a URL download link</small>
                            </div>
                            {/* Input for directory */}
                            <div className="form-group">
                                <label>Directory</label>
                                <input type="text" className="form-control" id="directory" placeholder="Enter a path" />
                                <small className="form-text text-muted">Enter the path to the directory where you want to archive the file</small>
                            </div>
                            {/*  Radio buttons for selecting data source type */}
                            <label>Source Type</label>
                            <div className="form-check">
                                <label className="form-check-label">
                                    <input type="radio" className="form-check-input" name="srctype" id="srctype1" value="FTP" />
                                    FTP
                                </label>
                            </div>
                            <div className="form-check">
                                <label className="form-check-label">
                                    <input type="radio" className="form-check-input" name="srctype" id="srctype2" value="URL" />
                                    URL
                                </label>
                            </div>
                            <div className="form-check">
                                <label className="form-check-label">
                                    <input type="radio" className="form-check-input" name="srctype" id="srctype3" value="Local File" />
                                    Local File
                                </label>
                            </div>
                            <br/>
                            {/* Input for username */}
                            <div className="form-group">
                                <label>Username</label>
                                <input type="text" className="form-control" id="username" placeholder="Enter a username" />
                                <small className="form-text text-muted">This is the username used to access your FTP</small>
                            </div>
                            {/* Input for password */}
                            <div className="form-group">
                                <label>Password</label>
                                <input type="password" className="form-control" id="password" placeholder="Enter a password" />
                                <small className="form-text text-muted">This is the password used to access your FTP</small>
                            </div>
                            {/* Input for file name*/}
                            <div className="form-group">
                                <label>File Name</label>
                                <input type="text" className="form-control" id="filename" placeholder="Enter the file name" />
                            </div>
                            {/* Input for column names array */}
                            <div className="form-group">
                                <label>Column Names</label>
                                <textarea className="form-control" id="columns" rows="4"></textarea>
                                <small className="form-text text-muted">Enter the column names seperated by commas. (Ex. first,last,date,etc.)</small>
                            </div>
                            <div className="float-right">
                                <button type="submit" className="btn btn-info">Submit</button>
                            </div>
                        </form>
                    </div>
                </div>
           </Fragment>
        )
    }

}

/*
const mapStateToProps = state => ({
    rules: state.rules.rules
});

export default connect(mapStateToProps, { getRules, deleteRules })(Rules);

*/

export default Rules;