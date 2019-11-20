import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import Header from './layout/Header';

export class FileHistory extends Component {
    state ={
        loading: true,
        table: null,
    }
    async componentDidMount(){
        const url = "http://127.0.0.1:8000/get_file_history";
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
                    <td className="col-2">{row.date_uploaded}</td>
                    <td className="col-4">{row.rows}</td>
                    <td className="col-2"><Link to="/fileview">View</Link></td>
                </tr>)
                }
                return table
            }
        return <div>Loading...</div>;
    }
    getName(){
        
        if (this.state.loading === false) {
            let name = []

            let row = this.state.table[0];
            name.push(<h3>{row.file_name}</h3>)
            return name
        }
        
        return <h3>Loading...</h3>;
    }

    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <div className="card card-body pl-4 pr-4 mt-4">{
                this.getName()
            }
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

export default FileHistory
