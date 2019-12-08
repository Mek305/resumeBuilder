import React, { Component } from 'react';


import './App.css';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import GetStarted from './components/Getstarted';
import Navi from './components/Navi.js';
import UserForm from './components/UserForm';

function App() {

   return (
     <Router>
       <div className ="App">
     <Navi />
       <Switch>
         <Route path ='/' exact component ={Home} />
         <Route path ='/getstarted' component = {GetStarted} />
         <Route path = '/resume' component ={UserForm}/>
       </Switch>
       
     </div>
     </Router>
   )
   
 }


 const Home = () =>(
   <div className ="head">
     <h1>Welcome to ResumeBuider Beta!!!</h1>
​
     <Link to="/getstarted">
       <button>Build Your Resume Now!!!</button>
     </Link>
   <hr></hr>
   <h1>Just click to insert custom pre-written bullets</h1>
     <p>Save time with thousands of pre-written “smart bullets” that you can click to plug-in to your resume.</p>
     <Link to="/getstarted">
       <button>Build Your Resume Now!!!</button>
     </Link>
  
   </div>
   
  
     

 )



export default App;
