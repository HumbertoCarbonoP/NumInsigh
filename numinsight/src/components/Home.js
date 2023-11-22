import '../styles/Home.css'

function HomePage(){
    return(
        <div className='hero-container'>
            <img src={require('../assets/images/Favicon.png')} alt='Logo NumInsight' className='main-image'/>
            <h2>NumInsight es un sitio web en el que encontrarás varios métodos utilizados para resolver problemas de análisis numérico.</h2>
        </div>
    )
}

export default HomePage;