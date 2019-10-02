import React from 'react'
import Head from 'next/head'
import Link from "next/link";
import "../style.css"

const Home = () => (
  <div>
    <Head>
        <title>Flex'n</title>
        <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500&display=swap" rel="stylesheet"/>
    </Head>

    <div className='hero'>
      <h1 className='title'>Welcome to Flex'n!</h1>
      <br/>
      <p className='description'>
        An application that automates data retrieval and facilitates data management.
        <hr/>
        <span>Frankie | Kamil | Taylor | James</span>
      </p>

      <div className='row'>
          <Link href="/dashboard">
            <a className='button'>
              <h3>Login</h3>
            </a>
          </Link>
      </div>
    </div>
  </div>
);

export default Home
