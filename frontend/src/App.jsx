import { useActionState } from 'react'
import './App.css'
import { search } from './helpers/Search';

function App() {
  const [result, searchAction, isPending] = useActionState(
    async (previousState, formData) => {
      return await search(formData);
    },
    null // initial state
  );

  return (
    <>
      <header className='connekt-outreach-header'>
        <div className='logo'>
          Connekt Outreach
        </div>
      </header>
      <section className='search-box'>
        <form action={searchAction}>
          <label>Enter who you are looking for</label>
          <input 
            name="query"
            placeholder='enter target description...' 
            required
          />
          <label>How many candidates should be outreach too.</label>
          <input 
            type='number'
            name='number'
            placeholder='enter qty...'
            min={1}
            max={50}
            required
          />
          <button type='submit' disabled={isPending}>
            {isPending ? 'Searching...' : 'Search'}
          </button>
        </form>

        {result?.success === false && (
          <p className='error'>Something went wrong: {result.message ?? 'please try again.'}</p>
        )}

        {result?.success && (
          <ul className='results'>
            {result.data?.map((person, i) => (
              <li key={i}>{person.first_name} — {person.job_company_name}</li>
            ))}
          </ul>
        )}
      </section>
    </>
  )
}

export default App