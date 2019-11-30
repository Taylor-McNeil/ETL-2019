import React, { Component, Fragment } from 'react'
import Header from './layout/Header';
import queryString from 'query-string';

export class FileView extends Component {
    state ={
        file_name: null,
        date_uploaded: null,
        loading: true,
        table: null,
    }
    async componentDidMount(){        
        const url_string = queryString.parse(this.props.location.search)

        const url = "http://127.0.0.1:8000/get_file_data/";
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
            body: JSON.stringify({
                "file_name": url_string.file_name,
                "date_uploaded": url_string.date_uploaded
                })
          });
        const data = await response.json();
        //console.log(data);
        this.setState({
            file_name: url_string.file_name,
            date_uploaded: url_string.date_uploaded,
            table: data, 
            loading: false});
    }
    getTable(){        
        if(this.state.loading === true ){
            return <div>Loading...</div>;            
        }
        else if(Object.keys(this.state.table).length == 0){
            return <div>Empty File</div>
        }
        else{
            let table = []
            for (let i = 0; i < this.state.table.length; i++) {
                let row = this.state.table[i];
                //console.log(Object.keys(row));
                //console.log(Object.values(row));
                row = Object.values(row);
                let col = [];
                for(let x = 0; x < row.length; x++){
                    col.push(<td className="col-2">{row[x]}</td>);
                }
                table.push(
                    <tr class = "row">
                    {col}
                    </tr>);
            }
            return table
        }
    }

    getTableHead(){
        if(this.state.loading === true ){
            return <div>Loading...</div>;            
        }
        else if(Object.keys(this.state.table).length == 0){
            return <h3>{this.state.file_name}</h3>
        }
        else{
            let table = []

            let head = this.state.table[0];
            let colHead = [];
            head = Object.keys(head);
            
            for(let x = 0; x < head.length; x++){
                colHead.push(<th className="col-2">{head[x]}</th>);
            }

            table.push(<thead>
                            <h3>{this.state.file_name}</h3>
                            <tr className="row">
                                {colHead}
                            </tr>
                        </thead>
            );
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
                            {this.getTableHead()}
                            <tbody>                  
                                {this.getTable()}
                            </tbody>
                        </table>   
                    </div> 
                </div>
            </Fragment>
        )
    }
}

export default FileView
