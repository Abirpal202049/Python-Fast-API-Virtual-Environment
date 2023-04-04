import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import { useState } from 'react'
import axios from 'axios'

export default function Home() {
  const [tweet, setTweet] = useState("")
  const [message, setMessage] = useState("")

  const handleSubmit = async (e) => {
    // e.preventDefault()
    console.log("This is submitted");
    console.log("Tweet", tweet);

    const { data } = await axios.get(`${process.env.BASE_URL_DEV}`)
    console.log("RES", data);

    if (tweet !== "") {
      const res = await axios.post(`${process.env.BASE_URL_DEV}predict?text=${tweet}`, null)
      console.log("RES", res);

      if (res.data.TAG.RandomForest === 1) {
        setMessage("Positive")
      }
      else {
        setMessage("Negative")
      }
    }
  }

  const handleOnchange = (e) => {
    setTweet(e.target.value)
    setMessage("")
  }

  return (
    <div>
      <h1>Sentiment Analysis</h1>
      <div style={{ 'width': "50%" }}>
        <textarea rows={10} cols={50} name="tweet" id="tweet" placeholder="Enter the tweet" onChange={handleOnchange} />
      </div>



      <button type="submit" onClick={handleSubmit}>Submit</button>


      <div>
        {message && message + " Sentement"}
      </div>
    </div>
  )
}

// Hello Noise team,
// I was buy smartwatch on 28 October. Watch is amazing but i have facing one issue with my smart watch from battery sides.
// When i was charging 100% then watch approx 15% dead every day thats okay but last 30% charging dead in 5-6 hours. I faced issue every time. I don't know this issue in only my watch or all noise watch. Please solve this problem.
