import '../styles/Methods.css'
import Button from "./Buttons";

function Metodos() {
    return (
        <div className='sections-container'>
            <div className='section'>
                <h2>Sección 1</h2>
                <Button text={"Bisección"} link='/biseccion'/>
                <Button text={"Regla Falsa"} link={'/reglaFalsa'}/>
                <Button text={"Punto Fijo CS"} link={'/puntoFijoCS'}/>
                <Button text={"Punto Fijo DC"} link={'/puntoFijoDC'}/>
                <Button text={"Newton-Raphson CS"} link={'/newtonCS'}/>
                <Button text={"Newton-Raphson CD"} link={'/newtonCD'}/>
                <Button text={"Secante"} link={'/secante'}/>
                <Button text={"Raíces Múltiples CS"} link={'/raicesMultiplesCS'} />
                <Button text={"Raíces Múltiples CD"} link={'/raicesMultiplesCD'} />
            </div>
            <div className='section'>
                <h2>Sección 2</h2>
                <Button text={"Jacobi Seidel"}/>
                <Button text={"Gauss"} />
                <Button text={"Sor"} />
            </div>
            <div className='section'>
            <h2>Sección 3</h2>
            <Button text={"Vandermonde"}/>
            <Button text={"Newton Interpolante"}/>
            <Button text={"Lagrange"}/>
            <Button text={"Spline"}/>
            </div>
        </div>
    )
}

export default Metodos;