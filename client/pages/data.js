import React, { Component } from 'react';
import Head from 'next/head';
import Layout from "../components/layout";
import "../style.css";

class Data extends React.Component {

    state = {
        cols : [{name:"", type:""}]
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
            <div className="container">

                <Layout />
                <div className="form-container">
                    <form onSubmit={this.handleSubmit} onChange={this.handleChange}>
                        <label htmlFor="tbname">Table Name</label>
                        <br/>
                        <input className="nsb" type="text" name="tbname" id="tbname" />
                        <br/>
                        <label htmlFor="colnum">Number of Columns </label>
                        <br/>
                        <input className="nsb" type="number" name="colnum" id="colnum" value={cols.length}/>
                        <br/>
                        <button onClick={this.addCol}>Add column</button>
                        {
                            cols.map((val, idx)=> {
                                let colId = `col-$(idx)`, typeId = `type-$(idx)`
                                return (
                                    <div key={idx}>
                                        <label htmlFor={colId}>{`Col #${idx+1}`}</label>
                                        <br/>
                                        <input
                                            type="text"
                                            name={colId}
                                            data-id={idx}
                                            id={colId}
                                            value={cols[idx].name}
                                            className="name"
                                        />
                                        <button onClick={() =>this.handleRemove(idx)} className="rmv">Remove</button>
                                        <br/>
                                    </div>
                                )
                            })
                        }
                        <br/>
                        <button>
                            <input className="sb" type="submit"/>
                        </button>
                        <br/>
                    </form>
                </div>

                {/*<div className="col-12">
                    <div className="card">
                        <div className="card-body">
                            <h4 className="card-title">Table Info</h4>
                            <form className="form-sample">
                                <p className="card-description">Metadata</p>
                                <div className="row">
                                    <div className="row-col">
                                        <div className="form-group row">
                                            <label className="label">Table Name</label>
                                            <div className="input">
                                                <input className="form-control">

                                                </input>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="row-col">
                                        <div className="form-group row">
                                            <label className="label"># of Columns</label>
                                            <div className="input">
                                                <input className="form-control">

                                                </input>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                                <div className="row">
                                <p>hi</p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>*/}
            </div>

        )
    }

}

export default Data;

