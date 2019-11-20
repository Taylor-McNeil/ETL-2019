import React, {Component, Fragment} from 'react';
import regenerator from "regenerator-runtime/runtime";
import { Link } from 'react-router-dom';
import Header from "./layout/Header";

export class Home extends Component {
    state ={
        loading: true,
        table: null,
    }
    async componentDidMount(){
        const url = "http://127.0.0.1:8000/get_rules";
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
        this.setState({table: data, loading: false});
    }


    getTable(){
        if (this.state.loading === false) {
            let table = []

            for (let i = 0; i < this.state.table.length; i++) {
                let row = this.state.table[i];
                console.log(row);
                table.push(<tr class = "row">
                    <td className="col-2">{row.file_id}</td>
                    <td className="col-4"><Link to="/filehistory">{row.file_name}</Link></td>
                    <td className="col-4">{row.last_update}</td>
                    <td className="col-2"><Link to="/rules">Edit</Link></td>
                </tr>)
                }
                return table
            }
        return <div>Loading...</div>;
    }


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
                            <tbody>
                            {
                            this.getTable()
                            }
                            </tbody>
                        </table>   
                    </div> 
                </div>
            </Fragment>
        )
    }
}

export default Home
