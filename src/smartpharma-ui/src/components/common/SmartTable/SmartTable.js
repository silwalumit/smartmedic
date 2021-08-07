import React from 'react'
import { Container } from '../Container'
import './table.scss';
import TableRow from './TableBody';
import TableHead from './TableHead';

const SmartTable = (props) => {
    return (
        <Container className={props.responsive && 'table-responsive'}>
            <table className="table table-striped table-sm" >
                <TableHead headers={props.headers} />
                <tbody>
                {props.dataSet.map((data,index )=> (
                    <TableRow
                        key={index}
                        headers={props.headers}
                        data={data} />
                ))}
                </tbody>
            </table>
        </Container>
    )
}

export default SmartTable
