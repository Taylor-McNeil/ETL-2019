import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addRules } from "../actions/rules";

export class RulesForm extends Component {
    state = {
        file_name: '',
        col_num: '',
        col_header: '',
    };

    static propTypes = {
        addRules: PropTypes.func.isRequired
    };

    onChange = e => this.setState({ [e.target.name]: e.target.value });

    onSubmit = e => {
        e.preventDefault();
        const { file_name, col_num, col_header } = this.state;
        const rules = { file_name, col_num, col_header };
        this.props.addRules(rules);
    };

    render() {
        const { file_name, col_num, col_header } = this.state;
        return (
            <div>
                <div className="card card-body mt-4 mb-4">
                    <h2>File Name</h2>
                    <input
                        className="form-control"
                        type="text"
                        name="file_name"
                        onChange={this.onChange}
                        value={file_name}
                        placeholder="File Name"
                    />
                </div>
                <div className="card card-body mt-4 mb-4">
                    <h2>New Column</h2>
                    <form onSubmit={this.onSubmit}>
                        <div className="form-group">
                            <div className="form-row">
                                <div className="col-2">
                                    <label>Column ID</label>
                                    <input
                                        className="form-control"
                                        type="text"
                                        name="col_num"
                                        onChange={this.onChange}
                                        value={col_num}
                                    />
                                </div>
                                <div className="col-10">
                                    <label>Column Header</label>
                                    <input
                                        className="form-control"
                                        type="text"
                                        name="col_header"
                                        onChange={this.onChange}
                                        value={col_header}
                                    />
                                </div>
                            </div>
                        </div>
                        <div className="form-group">
                            <button type="submit" className="btn btn-info">Add</button>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default connect(null, { addRules })(RulesForm);
