import React, { useState } from 'react';
import '../styles/Biseccion.css';
import PuntoFijoDCResult from './PuntoFijoDC-Result';

function PuntoFijoDC() {
    const [formState, setFormState] = useState({
        funcionF: '',
        funcionG: '',
        x_inferior: '',
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
            const response = await fetch('http://localhost:5000/puntoFijoDC', {
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
                        value={formState.funcion}
                        onChange={handleChange}
                        required
                        placeholder="Función f(x)"
                    />
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        name="funcionG"
                        value={formState.funcion}
                        onChange={handleChange}
                        required
                        placeholder="Función g(x)"
                    />
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        name="x_inferior"
                        value={formState.x_inferior}
                        onChange={handleChange}
                        required
                        placeholder="x inferior"
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
            <PuntoFijoDCResult result={resultData} />
        </div>
    );
}

export default PuntoFijoDC;
