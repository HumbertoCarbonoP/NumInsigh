import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import Metodos from './components/Methods';
import Ayuda from './components/Help';
import Sobre from './components/About';
import HomePage from './components/Home';
import Biseccion from './components/Biseccion';
import ReglaFalsa from './components/ReglaFalsa';
import PuntoFijoCS from './components/PuntoFijoCS';
import PuntoFijoDC from './components/PuntoFijoDC';
import NewtonCS from './components/NewtonCS';
import NewtonCD from './components/NewtonCD';
import Secante from './components/Secante';
import RaicesMultiplesCS from './components/RaicesMultiplesCS';
import RaicesMultiplesCD from './components/RaicesMultiplesCD';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/metodos' element={<Metodos />} />
          <Route path='/ayuda' element={<Ayuda />} />
          <Route path='/sobre' element={<Sobre />} />
          <Route path='/biseccion' element={<Biseccion />} />
          <Route path='/reglaFalsa' element={<ReglaFalsa />} />
          <Route path='/puntoFijoCS' element={<PuntoFijoCS />} />
          <Route path='/puntoFijoDC' element={<PuntoFijoDC />} />
          <Route path='/newtonCS' element={<NewtonCS />} />
          <Route path='/newtonCD' element={<NewtonCD />} />
          <Route path='/secante' element={<Secante />} />
          <Route path='/raicesMultiplesCS' element={<RaicesMultiplesCS />} />
          <Route path='/raicesMultiplesCD' element={<RaicesMultiplesCD />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;