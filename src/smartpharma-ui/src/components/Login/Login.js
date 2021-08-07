import React, { Component } from 'react';
import { Container } from '../common/Container';
import Button from '../common/Form/Button';
import { Input } from '../common/Form/Input';
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
                        <Container classes="mb-2" >
                            <Input
                                pattern = "[a-zA-Z]"
                                label="Username"
                                placeholder="Username"
                                valueChanged={value => this.handleChange('username', value)} />
                        </Container>
                        <Container classes="mb-2" >
                            <Input
                                type="password"
                                label="Password"
                                placeholder="Password"
                                valueChanged={value => this.handleChange('password', value)} />
                        </Container>
                        <Button
                            role ="submit"
                            label="Sign in"
                            disabled={this.disabled()} />
                    </form>
                </div>
            </div>
        );
    }
}


export default Login