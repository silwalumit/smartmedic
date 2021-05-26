import React, { Component } from 'react';
import { Container } from '../common/Container';
import SearchInput from '../common/SearchInput';

class Product extends Component {
 
    search(str) {
        console.log(str )
    }
    render() {
        return (
            <Container classes="d-flex justify-content-between row"> 
                <h2 className="h2 col text-muted">Product</h2>
                <Container classes="col-6 mb-2 mb-md-0">
                    <SearchInput search={str => this.search(str)}/>
                </Container>
            </Container>
        );
    }
}

export default Product;