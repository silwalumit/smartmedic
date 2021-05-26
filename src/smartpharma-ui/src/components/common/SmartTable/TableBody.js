import React from 'react';
import Checkbox from '../Checkbox';
import headerTypes from './constants';

const TableBody = (props) => {
    const { headers, data } = props;
    return (
        <tr>
            {headers.map((header, index) => (
                <td key={index}>
                    {data[header.key]}
                </td>
            ))}
        </tr>
        
    )
}

export default TableBody
