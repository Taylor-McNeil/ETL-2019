import React from 'react'
import Head from 'next/head'
import Link from "next/link";
import '../static/bootstrap.min.css';

const Home = () => (
  <div>
      <Head>
          <title>Flex</title>
      </Head>
      <div className="jumbotron text-center">
          <h1 className="display-4">Welcome to F /_ E X</h1>
          <p className="lead">An application that automates data retrieval and facilitates data management.</p>
          <hr className="my-4"/>
              <p>Frankie | Kamil | Taylor | James</p>
              <Link href="http://localhost:8000/accounts/login/">
                  <a className="btn btn-primary btn-lg" role="button">Login</a>
              </Link>
      </div>
  </div>
);

export default Home
