import React from 'react';
import { Input } from './Form/Input';


export const SearchInput = (props) => {
    return (
        <Input
            placeholder="Search"
            valueChanged={value => props.search(value)} />
    )
}

export default SearchInput
