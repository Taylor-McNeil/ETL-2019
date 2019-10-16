import React, { Component } from 'react';
import Head from 'next/head';
import Layout from "../components/layout";
import '../static/bootstrap.min.css';


class Data extends React.Component {

    state = {
        cols : [{name:"", type:""}],
        file:"",
        col_num:"",
    };

    handleChange = (e) => {
        if(["name", "type"].includes(e.target.className)) {
            let cols = [...this.state.cols];
            cols[e.target.dataset.id][e.target.className] = e.target.value;
            this.setState({ cols }, () => console.log(this.state.cols))
        } else {
            this.setState({[e.target.name]: e.target.value.toUpperCase()})
        }
    };

    addCol = (e) => {
        this.setState((prevState) => ({
            cols: [...prevState.cols, {name:"", type:""}],
        }));
    };

    handleRemove(idx) {
        this.state.cols.splice(idx,1)
        console.log(this.state.cols,"$$$$");
        this.setState({cols: this.state.cols})
    }

    handleSubmit = (e) => { e.preventDefault() };

    render () {
        let {cols} = this.state;
        return (
            <div>
                <Head>
                    <title>Data Form</title>
                </Head>
                <Layout/>
                <br/>
                <div className="container">
                    <h1>Metadata</h1>
                    <p className="lead">
                        The data submitted will be used to create a new table in the database as well as for comparison
                        with scanned files in our backend.
                    </p>
                    <hr />
                    <form onSubmit={this.handleSubmit} onChange={this.handleChange}>
                        <div className="form-row">
                            <div className="col-md-8">
                                <input type="text" className="form-control" placeholder="File Name"/>
                            </div>
                            <div className="col-md-2">
                                <input type="number" className="form-control" placeholder="# of Columns"/>
                            </div>
                            <div className="col-md-2">
                                <button type="button" className="btn btn-primary" onClick={this.addCol}>Add Col</button>
                            </div>
                            <hr />
                        </div>
                        <br />
                        {
                            cols.map((val,idx) => {
                                let colId = `col-$(idx)`, typeId = `type-$(idx)`;
                                return (
                                    <div>
                                        <div className="form-row mb-1" key={idx}>
                                            <div className="col-md-8">
                                                <input
                                                    type="text"
                                                    name={colId}
                                                    data-id={idx}
                                                    id={colId}
                                                    value={cols[idx].name}
                                                    placeholder={`Column ${idx+1}`}
                                                    className="form-control name"
                                                />
                                            </div>
                                            <div className="col-md-2">
                                                <input
                                                    type="text"
                                                    name={colId}
                                                    data-id={idx}
                                                    id={colId}
                                                    value={cols[idx].type}
                                                    placeholder="Data Type"
                                                    className="form-control name"
                                                />
                                            </div>
                                            <div className="col-md-2">
                                                <button type="button" className="btn btn-primary" onClick={() => this.handleRemove(idx)}>Remove</button>
                                            </div>
                                        </div>
                                    </div>
                                )
                            })
                        }
                        <div className="form-row">
                            <div className="col text-center">
                                <button type="submit" className="btn btn-primary">Submit</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

        )
    }

}

export default Data;

