import React from 'react';
import logo from './logo.svg';
import './App.css';

import Book from './components/RecipeDetail/RecipeDetail'
import RecipeDetail from './components/RecipeDetail/RecipeDetail';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <RecipeDetail></RecipeDetail>
      </header>
    </div>
  );
}

export default App;
