import '../styles/Biseccion-Result.css';

function SecanteResult({ result }) {
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
                                <th>x0</th>
                                <th>x1</th>
                                <th>x2</th>
                                <th>f(x2)</th>
                                <th>Error</th>
                            </tr>
                        </thead>
                        <tbody>
                            {result[1].map((_, index) => (
                                <tr key={index}>
                                    <td>{result[0][index]}</td>
                                    <td>{result[1][index]}</td>
                                    <td>{result[2][index]}</td>
                                    <td>{result[3][index]}</td>
                                    <td>{result[4][index]}</td>
                                    <td>{result[5][index]}</td>
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

export default SecanteResult;
