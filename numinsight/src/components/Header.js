import '../styles/Header.css'
import { Link } from 'react-router-dom';

function Header() {
    return (
        <div className="header-container">
            <div className='logo-container'>
                <Link to="/">
                    <img
                        className="logo"
                        src={require('../assets/images/Logo.png')}
                        alt="Logo NumInsight"
                    />
                </Link>
            </div>
            <div className='links-container'>
                <Link to="/metodos">Métodos</Link>
                <Link to="/ayuda">Ayuda</Link>
                <Link to="/sobre">Sobre NumInsight</Link>
            </div>
        </div>
    );
}

export default Header;