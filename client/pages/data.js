import React, { Component } from 'react';
import Head from 'next/head';
import Layout from "../components/layout";


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
            <div>
                <Head>
                    <title>Data Form</title>
                    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic"/>
                </Head>
                <Layout/>
                <div className="form-container">
                    <form onSubmit={this.handleSubmit} onChange={this.handleChange}>
                        <div className="field">
                            <label className="label" htmlFor="tbname">Table Name</label>
                            <div className="control">
                                <input className="nsb" type="text" name="tbname" id="tbname" />
                            </div>
                        </div>
                        <div className="field">
                            <label className="label" htmlFor="colnum"># of Columns </label>
                            <input className="nsb" type="number" name="colnum" id="colnum" value={cols.length}/>
                        </div>
                        <div className="control2">
                            <button className="button2" onClick={this.addCol}>Add column</button>
                            {
                                cols.map((val, idx)=> {
                                    let colId = `col-$(idx)`, typeId = `type-$(idx)`
                                    return (
                                        <div className="field2" key={idx}>
                                            <br/>
                                            <label className="label" htmlFor={colId}>{`Col #${idx+1}`}</label>
                                            <input
                                                type="text"
                                                name={colId}
                                                data-id={idx}
                                                id={colId}
                                                value={cols[idx].name}
                                                className="nsb2"
                                            />
                                            <button className="button2" onClick={() =>this.handleRemove(idx)}>Remove</button>
                                        </div>
                                    )
                                })
                            }
                        </div>
                        <div className="control2">
                            <button className="submit-btn" type="submit">Submit</button>
                        </div>

                    </form>
                </div>
            </div>

        )
    }

}

export default Data;

