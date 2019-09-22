import React from 'react';
import Navbar from "./navbar";
import Sidenav from "./sidenav";

const Layout = (props) => (
    <div>
        <Navbar/>
        <Sidenav/>
        {props.children}
    </div>
);

export default Layout;
