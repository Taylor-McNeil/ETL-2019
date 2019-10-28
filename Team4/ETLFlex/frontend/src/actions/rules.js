import axios from 'axios';

import {GET_RULES, DELETE_RULES, ADD_RULES } from "./types";

// GET RULES
export const getRules = () => dispatch => {
    axios.get('/api/rules/')
        .then(res => {
            dispatch({
                type: GET_RULES,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
};

// DELETE RULES
export const deleteRules = (id) => dispatch => {
    axios.delete(`/api/rules/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_RULES,
                payload: id
            });
        })
        .catch(err => console.log(err));
};

// ADD RULES
export const addRules = (rules) => dispatch => {
    axios.post("/api/rules/",rules)
        .then(res => {
            dispatch({
                type: ADD_RULES,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
};
