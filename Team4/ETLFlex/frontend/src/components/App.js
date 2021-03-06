import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom";

import Dashboard from "./layout/Dashboard";
import Home from "./Home";
import Rules from "./Rules";
import Landing from "./Landing";
import FileHistory from "./FileHistory";
import FileView from "./FileView";

import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <Switch>
                            <Route exact path="/landing" component={Landing} />
                            <Route exact path="/" component={Home} />
                            <Route exact path="/rules" component={Rules} />
                            <Route exact path="/filehistory" component={FileHistory} />
                            <Route exact path="/fileview" component={FileView} />
                        </Switch>
                    </Fragment>
                </Router>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
