import React from 'react'
import Checkbox from '../Form/Checkbox'

const TableHead = (props) => {
    return (
        <thead>
            <tr className = "table-dark">
                {props.headers.map((header, key) => (
                    <th key={key}>
                        {header.selectable ? (
                            <Checkbox
                                checked={header.selected}
                                onClick={e => header.onChange(!header.selected)} />
                        ) : header.label}
                    </th>
                ))}
            </tr>
        </thead>
    )
}

export default TableHead
