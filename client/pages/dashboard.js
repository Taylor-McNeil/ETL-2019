import React from 'react';
import Head from 'next/head'
import Layout from "../components/layout";
import '../static/bootstrap.min.css';

const Dash = () => (
    <div>
        <Head>
            <title>Dashboard</title>
        </Head>
        <Layout>
            <div className="container mt-5">
                <div className="row">
                    <div className="col-md-3">
                        <div className="card border-info mb-3">
                            <div className="card-header">Taylor</div>
                            <div className="card-body">
                                <h4 className="card-title">Team Lead</h4>
                                <p className="card-text">Manage Project Tasks and Files</p>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="card border-info mb-3">
                            <div className="card-header">Frankie</div>
                            <div className="card-body">
                                <h4 className="card-title">Backend Dev</h4>
                                <p className="card-text">Connect to Data Source and Database Management</p>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="card border-info mb-3">
                            <div className="card-header">Kamil</div>
                            <div className="card-body">
                                <h4 className="card-title">Full Stack Dev</h4>
                                <p className="card-text">React/Django Stack</p>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="card border-info mb-3">
                            <div className="card-header">James</div>
                            <div className="card-body">
                                <h4 className="card-title">Full Stack Dev</h4>
                                <p className="card-text">React/Django Stack</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    </div>
);

export default Dash;
