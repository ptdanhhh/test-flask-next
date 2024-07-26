"use client";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Check() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    // Fetch session data from the Flask backend using axios
    axios
      .get("http://localhost:8001/check") // Replace with your backend URL
      .then((response) => {
        const data = response.data;
        if (data.status === "success") {
          setMessage(data.message);
        } else {
          setMessage("Failed to fetch session data");
        }
      })
      .catch((error) => {
        console.error("Error fetching session data:", error);
        setMessage("An error occurred");
      });
  }, []);

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
}
