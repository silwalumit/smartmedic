import React from 'react'
import Checkbox from '../Checkbox'

const TableHead = (props) => {
    return (
        <thead>
            <tr>
                {props.headers.map((header, index) => (
                    <th key={index}>
                        {header.selectable ? (
                            <Checkbox checked={header.selected} />
                        ) : header.label}
                    </th>
                ))}
            </tr>
        </thead>
    )
}

export default TableHead
