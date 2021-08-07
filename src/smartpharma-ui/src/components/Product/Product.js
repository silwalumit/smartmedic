import React, { Component } from 'react';
import { Container } from '../common/Container';
import Modal from '../common/Modal/Modal';
import SmartTable from '../common/SmartTable/SmartTable';
import SearchInput from '../common/SearchInput';
import Button from '../common/Form/Button';


class Product extends Component {

    constructor() {
        super();
        this.state = {
            showModal: false,
            products: {
                dataSet: [
                    {
                        productName: 'Pantop',
                        unitPrice: 8.00,
                        tax: '13%',
                        discount: '10%',
                    },
                    {
                        productName: 'Dilzem 30',
                        unitPrice: 20.00,
                        tax: '13%',
                        discount: '10%'
                    }
                ],
                headers: [
                    { key: 'select', selectable: true, selected: false, onChange: () => this.selectAll() },
                    { key: 'productName', label: 'Product Name' },
                    { key: 'unitPrice', label: 'Unit Price' },
                    { key: 'tax', label: 'Tax' },
                    { key: 'discount', label: 'Discount' }
                ]
            }
        }
    }
    selectAll() {
        console.log('hello')
    }
    search(str) {
        console.log(str)
    }

    render() {
        const products = this.state.products;
        return (
            <>
                <Container classes="d-flex justify-content-between row pb-3 mb-3 border-bottom">
                    <h2 className="h2 col text-muted">Product</h2>
                    <Container classes="col-lg-6 mb-2 mb-md-0">
                        <SearchInput search={str => this.search(str)} />
                    </Container>
                </Container>
                <Container className="pb-3">
                    <Button type='button' label='Add' classes='btn-sm'
                        onClick={() => {
                            this.setState(prevState => ({
                                ...prevState,
                                showModal: true
                            }))
                        }}>
                    </Button>
                </Container>

                <Modal title="Add Product" show={this.state.showModal} />
                <SmartTable
                    dataSet={products.dataSet}
                    headers={products.headers}></SmartTable>

            </>
        );
    }
}

export default Product;