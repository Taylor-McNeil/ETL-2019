import React, { Component, Fragment } from 'react'
import Header from './layout/Header';

export class FileView extends Component {
    state ={
        loading: true,
        table: null,
    }
    async componentDidMount(){
        const url = "http://127.0.0.1:8000/get_file_data";
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
                    <td className="col-2">{row.name}</td>
                    <td className="col-2">{row.age}</td>
                    <td className="col-4">{row.profession}</td>
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
                                <h3>F1.txt</h3>
                                <tr className="row">
                                    <th className="col-2">Name</th>
                                    <th className="col-2">Age</th>
                                    <th className="col-4">Profession</th>
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

export default FileView
