import React, { Component } from 'react';

import Header from './Header';

export class Dashboard extends Component {
    render(props) {
        return (
            <div>
                <Header />
                <br />
                {props}
            </div>
        )
    }
}

export default Dashboard
