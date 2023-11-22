import React, { useState } from 'react';
import '../styles/Biseccion.css';
import RaicesMultiplesResult from './RaicesMultiples-Result';

function RaicesMultiplesCS() {
    const [formState, setFormState] = useState({
        funcionF: '',
        funcionF1: '',
        x0: '',
        tolerancia: '',
        iteraciones: ''
    });

    const handleChange = (e) => {
        setFormState({
            ...formState,
            [e.target.name]: e.target.value
        });
    };

    const [resultData, setResultData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:5000/raicesMultiplesCS', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formState),
            });
            const data = await response.json();
            setResultData(data);
        } catch (error) {
            console.error('Error al enviar formulario:', error);
        }
    };


    return (
        <div>
            <form onSubmit={handleSubmit} className="form">
                <div className="input-container">
                    <input
                        type="text"
                        name="funcionF"
                        value={formState.funcionF}
                        onChange={handleChange}
                        required
                        placeholder="Función f(x)"
                    />
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        name="funcionF1"
                        value={formState.funcionF1}
                        onChange={handleChange}
                        required
                        placeholder="Funcion f'(x)"
                    />
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        name="x0"
                        value={formState.x0}
                        onChange={handleChange}
                        required
                        placeholder="x0"
                    />
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        name="tolerancia"
                        value={formState.tolerancia}
                        onChange={handleChange}
                        required
                        placeholder="Tolerancia"
                    />
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        name="iteraciones"
                        value={formState.iteraciones}
                        onChange={handleChange}
                        required
                        placeholder="Número de iteraciones"
                    />
                </div>
                <button type="submit" className="submit-button">Calcular</button>
            </form>
            <RaicesMultiplesResult result={resultData} />
        </div>
    );
}

export default RaicesMultiplesCS;
