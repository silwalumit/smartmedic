import React, { Component } from 'react';
import { Container } from '../common/Container';
import { Input } from '../common/Input';
import styles from './loginStyle.module.css'

class Login extends Component {

    constructor() {
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
        this.state = {
            username: "",
            password: "",
        }
    }
    disabled() {
        return !(this.state.password && this.state.username)
    }
    handleChange(key, value) {
        this.setState(prevState => ({
            ...prevState,
            [key]: value
        }));
    }
    handleSubmit(e) {
        e.preventDefault();
    }
    render() {
        return (
            <div className={styles.container}>
                <div className={styles.loginForm}>
                    <form onSubmit={this.handleSubmit} noValidate>
                        <Container classess="mb-2" >
                            <Input
                                pattern = "[a-zA-Z]"
                                label="username"
                                placeholder="username"
                                valueChanged={value => this.handleChange('username', value)} />
                        </Container>
                        <Container classess="mb-2" >
                            <Input
                                type="password"
                                label="password"
                                placeholder="password"
                                valueChanged={value => this.handleChange('password', value)} />
                        </Container>

                        <button disabled={this.disabled()} className={`w-100 btn btn-lg ${this.disabled() ? 'btn-secondary' : 'btn-primary'}`} type="submit">Sign in</button>
                    </form>
                </div>
            </div>
        );
    }
}


export default Login