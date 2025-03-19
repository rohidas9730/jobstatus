import { useEffect, useState } from "react";
import axios from "axios";
// import Navbar from "./components/Navbar";
import DropdownForm from "./components/DropdownForm";
import JobTable from "./components/JobTable";
// import TodoForm from "./components/TodoForm";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  const [jobs, setJobs] = useState([]);

  const fetchJobs = async () => {
    try {
      const response = await axios.get("http://192.168.1.2:8000/");
      setJobs(response.data.jobs);
    } catch (error) {
      console.error("Error fetching jobs:", error);
    }
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  const handleRun = async () => {
    try {
      const response = await fetch("http://192.168.1.2:8000/run-job", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          menu: selectedFile, // Ensure selectedFile is defined
          option_id: optionId, // Ensure optionId is defined
          option_text: fileName, // Ensure fileName is defined
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to run job");
      }

      const data = await response.json();
      console.log("Job started:", data);
      fetchJobs(); // Refresh the job list
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    // <div style={{ padding: "20px", width: "90vw" }}>
    //   <Navbar />
    //   <h1>Playbook Job Manager</h1>
    //   <DropdownForm fetchJobs={fetchJobs} />
    //   <hr />
    //   <JobTable jobs={jobs} />
    // </div>

    <div style={{ padding: "20px", width: "90vw" }}>
      <h1>Job Management System by Quantum</h1>
      <DropdownForm fetchJobs={setJobs} />
      <JobTable jobs={jobs} />
    </div>
  );
};

export default App;
// return (
//   <div>
//     <Navbar />
//     <DropdownForm />
//     <JobTable jobs={jobs} />
//     {/* <TodoForm addTodo={addTodo} /> */}
//   </div>
// );
