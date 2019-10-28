import { GET_RULES, DELETE_RULES, ADD_RULES } from "../actions/types.js";

const initialState = {
    rules: []
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_RULES:
            return {
                ...state,
                rules: action.payload
            };
        case DELETE_RULES:
            return {
                ...state,
                rules: state.rules.filter(rules => rules.id !== action.payload)
            };
        case ADD_RULES:
            return {
                ...state,
                rules: [...state.rules, action.payload]
            };
        default:
            return state;
    }
}
