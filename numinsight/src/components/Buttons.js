import '../styles/Button.css';
import { Link } from 'react-router-dom';

function Button({ text, link}){
    return(
        <Link to={ link }>
            <button className='method-button'>{text}</button>
        </Link>
    )
}

export default Button;