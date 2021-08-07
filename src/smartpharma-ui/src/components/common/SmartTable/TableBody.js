import React from 'react';
import Checkbox from '../Form/Checkbox';
import headerTypes from './constants';

const TableRow = (props) => {
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

export default TableRow
