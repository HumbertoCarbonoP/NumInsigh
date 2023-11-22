import '../styles/Biseccion-Result.css';

function BiseccionResult({ result }) {
    const hasData = result && Array.isArray(result) && result.length > 6;
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
                                <th>x_inferior</th>
                                <th>xm</th>
                                <th>x_superior</th>
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
                                    <td>{result[5][index]}</td>
                                    <td>{result[6][index]}</td>
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

export default BiseccionResult;
