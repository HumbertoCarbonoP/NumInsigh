import '../styles/Biseccion-Result.css';

function PuntoFijoCSResult({ result }) {
    console.log(result);
    const hasData = result && Array.isArray(result) && result.length > 4;
    const isString = typeof result === 'string';

    return (
        <div className='biseccion-result'>
            {hasData ? (
                <div>
                    <p className='response'>{result[0]}</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Iteración</th>
                                <th>xn</th>
                                <th>fm</th>
                                <th>Error</th>
                            </tr>
                        </thead>
                        <tbody>
                            {result[1].map((_, index) => (
                                <tr key={index}>
                                    <td>{result[1][index]}</td>
                                    <td>{result[2][index]}</td>
                                    <td>{result[3][index]}</td>
                                    <td>{result[4][index]}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            ) : isString ? (
                <p className='response'>{result}</p>
            ) : (
                <p className='response'>No hay datos para mostrar</p>
            )}
        </div>
    );
}

export default PuntoFijoCSResult;
