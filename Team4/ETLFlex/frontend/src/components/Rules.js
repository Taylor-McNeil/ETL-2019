import React, {Component, Fragment} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getRules, deleteRules } from "../actions/rules";
import { Link } from 'react-router-dom';

import rules from "../reducers/rules";
import RulesForm from "./RulesForm";
import Header from "./layout/Header";

class Rules extends Component {
    static propTypes = {
        rules: PropTypes.array.isRequired,
        getRules: PropTypes.func.isRequired,
        deleteRules: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getRules();
    }

    render () {
        return (
           <Fragment>
               <Header />
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
           </Fragment>
        )
    }

}

const mapStateToProps = state => ({
    rules: state.rules.rules
});

export default connect(mapStateToProps, { getRules, deleteRules })(Rules);

