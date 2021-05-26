import React from 'react'
import { Container } from '../Container'
import './table.css';
import TableBody from './TableBody';
import TableHead from './TableHead';

const SmartTable = (props) => {
    return (
        <Container className={props.responsive && 'table-responsive'}>
            <table className="table table-sm table-striped" >
                <TableHead {...props} />
                {props.dataSet.map((data => (
                    <TableBody
                        headers={props.headers}
                        data={data} />
                )))}
            </table>
        </Container>
    )
}

export default SmartTable
