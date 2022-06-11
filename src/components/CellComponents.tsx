import React, {FC} from 'react';
import {Cell} from "../models/Cell";

interface CellProps {
    cell: Cell;
    selected: boolean;
    click: (cell: Cell) => void;
}

const CellComponents: FC<CellProps> = ({cell, selected, click}) => {
    return (
        <div
            onClick={() => click(cell)}
            className={["cell", cell.color, selected ? "selected" : ""].join(' ')}
            style={{background: cell.available && cell.figure ? 'green' : ''}}
        >
            {cell.available && !cell.figure && <div className={"available"}/>}
            {cell.figure?.logo && <img src={cell.figure.logo} alt=""/>}
        </div>
    );
};

export default CellComponents;