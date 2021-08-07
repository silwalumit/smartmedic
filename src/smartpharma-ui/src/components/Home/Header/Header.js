import React from 'react';
import { Container } from '../../common/Container';
import { Input } from '../../common/Form/Input'
import './header.scss'

const Header = () => {

    return (
        <header className="row navbar">
            <a href="#" className="navbar-brand col-md-3 col-lg-2">
               Smart Pharma
            </a>
            <Container className="col-lg-8 col-md-6">
                <Input
                    classes="form-control-dark"
                    noFloat
                    placeholder="search products"
                    valueChanged={value => console.log(value)} />
            </Container>
        </header>
    );
}

export default Header;
