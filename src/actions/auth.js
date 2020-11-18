import axios from 'axios'
import {setAlert} from './alert'
import {LOGIN_FAIL, LOGIN_SUCCESS, LOGOUT, SIGNUP_FAIL, SIGNUP_SUCCESS} from './types'

export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'content-Type': 'application/json'
        }
    };
    const body = JSON.stringify({email, password});
    try {
        const res = await axios.post('http://127.0.0.1:8000/api/token/', body, config);
        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        });
        dispatch(setAlert('Authenticated Successfuly', 'success',));
    } catch (error) {
        dispatch({
            type: LOGIN_FAIL,
        });
        dispatch(setAlert('Authentication failed!', 'error',));

    }
};
export const signup = ({name, email, password, password2}) => async dispatch => {
    const config = {
        headers: {
            'content-Type': 'application/json'
        }
    };
    const body = JSON.stringify({name, email, password, password2});
    try {
        const res = await axios.post('http://127.0.0.1:8000/api/accounts/signup/', body, config);
        dispatch({
            type: SIGNUP_SUCCESS,
            payload: res.data
        });
        dispatch(login(email, password));
    } catch (error) {
        dispatch({
            type: SIGNUP_FAIL,
        });
        dispatch(setAlert('Authentication failed!', 'error',));

    }
};
export const logout = () => dispatch => {
    dispatch(setAlert('logout successfully', 'success'));
    dispatch({type: LOGOUT});

};
