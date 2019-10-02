import React from 'react';
import Nav from './nav';
import "../style.css";

const Layout = (props) => (
    <div>
        <Nav/>
        {props.children}
    </div>
);

export default Layout;
