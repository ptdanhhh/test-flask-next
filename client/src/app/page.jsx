"use client";
import axios from "axios";

export default function Home() {
  const url = "http://127.0.0.1:8001/hello";
  const url2 = "http://127.0.0.1:8001/test";

  // const testFetch = () => {
  //   fetch(url)
  //     .then((response) => response.json())
  //     .then((data) => console.log(data))
  //     .catch((err) => console.error(err));
  // };

  const testFetch = async () => {
    try {
      const response = await axios.get(url);
      console.log(response.data);
    } catch (error) {
      console.error("Oh no!!!", error);
    }
  };

  // const testFetch2 = () => {
  //   fetch(url2)
  //     .then((response) => response.json())
  //     .then((data) => console.log(data))
  //     .catch((err) => console.error(err));
  // };

  const testFetch2 = async () => {
    try {
      const response = await axios.get(url2);
      console.log(response.data);
    } catch (error) {
      console.error("Oh no!!!", error);
    }
  };

  return (
    <>
      <button onClick={testFetch}>Click</button>
      <br></br>
      <button onClick={testFetch2}>Click2</button>
    </>
  );
}
