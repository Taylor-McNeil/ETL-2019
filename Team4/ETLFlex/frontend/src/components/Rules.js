import React, {Component, Fragment} from 'react';
import { Formik, FieldArray, Field } from 'formik';

import Header from "./layout/Header";

class Rules extends Component {

    render () {
        return (
           <Fragment>
               <Header />
               <Formik
                   initialValues={{ src: '', directory: '', type: '', username: '', password: '', file_name: '', col: []}}
                   validate={values => {
                       const errors = {};
                       if (!values.type) {
                           errors.type = ' Source Type is Required';
                       }
                       if (!values.file_name) {
                           errors.file_name = ' File Name is Required';
                       }
                       return errors;
                   }}
                   onSubmit={(values, { setSubmitting }) => {
                        let url = "http://127.0.0.1:8000/submit_rule/";
                        fetch(url, {
                            method: 'POST',
                            headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json'
                                },
                            body: JSON.stringify(values)
                            }).then((response) => response.json())
                            .then((responseJson) => {
                                alert(responseJson);

                            })
                        setSubmitting(false);
                       /*setTimeout(() => {
                           alert(JSON.stringify(values,null,2));
                           console.log(JSON.stringify(values, null,2));
                           setSubmitting(false);
                       }, 400);*/
                   }}
               >
                   {({
                         values,
                         errors,
                         touched,
                         handleChange,
                         handleBlur,
                         handleSubmit,
                         isSubmitting,
                         setFieldValue,
                     }) => (
                       <div className="container">
                           <div className="card card-body p-4 mt-4">
                               <form onSubmit={handleSubmit}>
                                   <div className="form-group">
                                       <label>Data Source</label>
                                       <input
                                           type="text"
                                           name="src"
                                           onChange={handleChange}
                                           onBlur={handleBlur}
                                           value={values.src}
                                           className="form-control"
                                       />
                                       <small className="form-text text-muted">Enter the FTP address or a URL download link</small>
                                   </div>
                                   <div className="form-group">
                                       <label>Directory</label>
                                       <input
                                           type="text"
                                           name="directory"
                                           onChange={handleChange}
                                           onBlur={handleBlur}
                                           value={values.directory}
                                           className="form-control"
                                       />
                                       <small className="form-text text-muted">Enter the path to the directory where you want to archive the file</small>
                                   </div>
                                   <div className="form-group">
                                       <label>Source Type</label>
                                       <div className="form-check">
                                           <label className="form-check-label">
                                               <input
                                                   className="form-check-input"
                                                   type="radio"
                                                   name="type"
                                                   value="FTP"
                                                   checked={values.type === "FTP"}
                                                   onChange={() => setFieldValue("type", "FTP")}
                                               />FTP
                                           </label>
                                       </div>
                                       <div className="form-check">
                                           <label className="form-check-label">
                                               <input
                                                   className="form-check-input"
                                                   type="radio"
                                                   name="type"
                                                   value="URL"
                                                   checked={values.type === "URL"}
                                                   onChange={() => setFieldValue("type", "URL")}
                                               />URL
                                           </label>
                                       </div>
                                       <div className="form-check">
                                           <label className="form-check-label">
                                               <input
                                                   className="form-check-input"
                                                   type="radio"
                                                   name="type"
                                                   value="local"
                                                   checked={values.type === "local"}
                                                   onChange={() => setFieldValue("type", "local")}
                                               />Local File
                                           </label>
                                       </div>
                                       <p className="text-danger">{errors.type && touched.type && errors.type}</p>
                                   </div>
                                   <br />
                                   <div className="form-group">
                                       <label>Username</label>
                                       <input
                                           type="text"
                                           name="username"
                                           onChange={handleChange}
                                           onBlur={handleBlur}
                                           value={values.username}
                                           className="form-control"
                                       />
                                       <small className="form-text text-muted">This is the username used to access your FTP</small>
                                   </div>
                                   <div className="form-group">
                                       <label>Password</label>
                                       <input
                                           type="password"
                                           name="password"
                                           onChange={handleChange}
                                           onBlur={handleBlur}
                                           value={values.password}
                                           className="form-control"
                                       />
                                       <small className="form-text text-muted">This is the password used to access your FTP</small>
                                   </div>
                                   <div className="form-group">
                                       <label>File Name</label>
                                       <input
                                           type="text"
                                           name="file_name"
                                           onChange={handleChange}
                                           onBlur={handleBlur}
                                           value={values.file_name}
                                           className="form-control"
                                       />
                                       <p className="text-danger">{errors.file_name && touched.file_name && errors.file_name}</p>
                                   </div>
                                   <label>Columns</label>
                                   <FieldArray
                                       name="col"
                                       render={arrayHelpers => (
                                           <div>
                                               {values.col && values.col.length > 0 ? (
                                                   values.col.map((col, index) => (
                                                       <div className="input-group" key={index}>
                                                           <Field className="form-control" name={`col.${index}`} />
                                                           <div className="input-group-append">
                                                               <button
                                                                   className="btn btn-outline-info"
                                                                   type="button"
                                                                   onClick={() => arrayHelpers.remove(index)} // remove a friend from the list
                                                               >
                                                                   -
                                                               </button>
                                                               <button
                                                                   className="btn btn-outline-info"
                                                                   type="button"
                                                                   onClick={() => arrayHelpers.insert(index+1, '')} // insert an empty string at a position
                                                               >
                                                                   +
                                                               </button>
                                                           </div>
                                                       </div>
                                                   ))
                                               ) : (
                                                   <button className="btn btn-outline-info" type="button" onClick={() => arrayHelpers.push('')}>
                                                       {/* show this when user has removed all friends from the list */}
                                                       Add a Column
                                                   </button>
                                               )}
                                           </div>
                                       )}
                                   />
                                   <div className="float-right mt-3">
                                       <button className="btn btn-info" type="submit" disabled={isSubmitting}>Submit</button>
                                   </div>
                               </form>
                           </div>
                       </div>
                   )}
               </Formik>
           </Fragment>
        )
    }

}

export default Rules;
