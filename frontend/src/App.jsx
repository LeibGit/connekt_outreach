import { useState } from 'react'
import './App.css'
import { search } from './helpers/Search';

function App() {
  return (
    <>
      <header className='connekt-outreach-header'>
        <div className='logo'>
          Connekt Outreach
        </div>
      </header>
      <section className='search-box'>
        <form action={search}>
          <label>Enter who you are looking for</label>
          <input 
            name="query"
            placeholder='enter target description...' 
            required
            />
          <button type='submit'>Search</button>

        </form>
      </section>
    </>
  )
}

export default App
