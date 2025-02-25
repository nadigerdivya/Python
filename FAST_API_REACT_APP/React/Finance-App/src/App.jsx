import { useState, useRef, useEffect } from 'react'
import './App.css'
import api from './api'

function App() {
  const [transactions, setTransactions] = useState([]);
  const currentYear = new Date().getFullYear();

  //input refs
  const amountRef = useRef(null);
  const categoryRef = useRef(null);
  const descriptionRef = useRef(null);
  const isIncomeRef = useRef(null);
  const dateRef = useRef(null);

  //Form Submit
  const handleSubmit = async () => {

    let transactionObj = {
      amount: amountRef.current.value,
      category: categoryRef.current.value,
      description: descriptionRef.current.value,
      is_income: isIncomeRef.current.checked,
      date: dateRef.current.value
    };

    try {
      await api.post('/transactions/', transactionObj);
      fetchTransactions();
    } catch (error) {
      console.error('Error submitting transaction:', error);
    }
  }

  //get transactions
  const fetchTransactions = async () => {
    const response = await api.get('/transactions');
    setTransactions(response.data)
  }

  useEffect(() => {
    fetchTransactions();
  }, []);

  //Form Clear
  const handleClear = () => {
    amountRef.current.value = '',
      categoryRef.current.value = '',
      descriptionRef.current.value = '',
      isIncomeRef.current.checked = false,
      dateRef.current.value = ''
  }

  return (
    <>
      <h1 className="text-3xl font-bold text-indigo-500 mb-6">Finance App</h1>
      <hr />
      <div className="finance-details flex flex-row p-4">
        <div className="form p-4">
          <form className="w-full max-w-lg" onSubmit={handleSubmit}>
            <div>
              <div className="flex flex-wrap -mx-3 mb-6">
                <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="amount">
                    Amount
                  </label>
                  <input className="appearance-none block w-full text-gray-700 border
                  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="amount" name="amount"
                    type="text" placeholder="Enter Amount" ref={amountRef} required />
                </div>
                <div className="w-full md:w-1/2 px-3">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="category">
                    Category
                  </label>
                  <input className="appearance-none block w-fulltext-gray-700 border 
                rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="category"
                    id="category" type="text" placeholder="Enter category" required ref={categoryRef} />
                </div>
              </div>
              <div className="flex flex-wrap -mx-3 mb-6">
                <div className="w-full px-3">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="description">
                    Description
                  </label>
                  <input className="appearance-none block w-full text-gray-700 border 
                rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="description"
                    id="description" type="text" placeholder="Enter description" ref={descriptionRef} />
                </div>
              </div>
              <div className="flex flex-wrap -mx-3 mb-6">
                <div className="w-full px-3">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="is_income">
                    Is income
                  </label>
                  <div className=" group grid size-4 grid-cols-1">
                    <input id="is_income" aria-describedby="is_income" name="is_income" type="checkbox" className="col-start-1 
                  row-start-1 appearance-none rounded-sm border border-gray-300 bg-white checked:border-indigo-600 
                  checked:bg-indigo-600 indeterminate:border-indigo-600 indeterminate:bg-indigo-600 focus-visible:outline-2 
                  focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:border-gray-300 disabled:bg-gray-100 
                  disabled:checked:bg-gray-100 forced-colors:appearance-auto" ref={isIncomeRef} />
                    <svg className="pointer-events-none col-start-1 row-start-1 size-3.5 self-center justify-self-center stroke-white group-has-disabled:stroke-gray-950/25" viewBox="0 0 14 14" fill="none">
                      <path className="opacity-0 group-has-checked:opacity-100" d="M3 8L6 11L11 3.5" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                      <path className="opacity-0 group-has-indeterminate:opacity-100" d="M3 7H11" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                  </div>
                </div>
              </div>
              <div className="flex flex-wrap -mx-3 mb-6">
                <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="date">
                    Date
                  </label>
                  <input className="appearance-none block w-full text-gray-700 border border-gray-200 
                    rounded py-3 px-4 mb-6 leading-tight focus: outline-none focus: bg-white focus: border-gray-500" name="date"
                    id="date" type="date" ref={dateRef} />
                </div>
              </div>
            </div>
            <div className="mt-6 flex items-center gap-x-6">
              <button type="submit" className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
              <button type="button" className="text-sm/6 font-semibold text-gray-900" onClick={handleClear}>Cancel</button>

            </div>
          </form>
        </div>
        <div className="inline-block h-[500px] min-h-[1em] w-0.5 self-stretch bg-neutral-100 dark:bg-white/10 margin-20"></div>


        <div className="relative overflow-x-auto m-12">
          <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th scope="col" className="px-6 py-3">
                  Amount
                </th>
                <th scope="col" className="px-6 py-3">
                  Category
                </th>
                <th scope="col" className="px-6 py-3">
                  Description
                </th>
                <th scope="col" className="px-6 py-3">
                  Is Income?
                </th>
                <th scope="col" className="px-6 py-3">
                  Date
                </th>
              </tr>
            </thead>
            <tbody>
              {
                transactions.map((data, index) => {
                  return (
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200" key={index}>
                      <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        {data.amount}
                      </th>
                      <td className="px-6 py-4">
                        {data.category}
                      </td>
                      <td className="px-6 py-4">
                        {data.description}
                      </td>
                      <td className="px-6 py-4">
                        {data.is_income ? 'Yes' : 'No'}
                      </td>
                      <td className="px-6 py-4">
                        {data.date}
                      </td>
                    </tr>
                  )
                })
              }
            </tbody>
          </table>
        </div>

      </div>
      <hr />
      <footer className="text-sm text-center">&copy; {currentYear} Finance App. All rights reserved.</footer>
    </>
  )
}

export default App
