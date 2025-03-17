// ##########################################################################################################################
// import { useState } from "react";
// import axios from "axios";
// import PropTypes from "prop-types";

// const DropdownForm = ({ fetchJobs }) => {
//   const [menu, setMenu] = useState("");
//   const [optionId, setOptionId] = useState("");
//   const [optionText, setOptionText] = useState("");

//   const handleChange = (e) => {
//     const selectedOption = e.target.options[e.target.selectedIndex];
//     setMenu(e.target.value);
//     setOptionId(selectedOption.id);
//     setOptionText(selectedOption.text);
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     // Add "In Progress" job to the list
//     const inProgressJob = {
//       id: Date.now(), // Temporary unique ID
//       job_id: optionId,
//       playbook: optionText,
//       date: new Date().toISOString().split("T")[0],
//       start_time: new Date().toLocaleTimeString(),
//       end_time: "--",
//       duration: "--",
//       status: "In Progress",
//     };

//     fetchJobs((prevJobs) => [inProgressJob, ...prevJobs]);

//     try {
//       const response = await axios.post("http://localhost:5000/", {
//         menu: menu,
//         option_id: optionId,
//         option_text: optionText,
//       });

//       console.log("Job Submitted:", response.data);
//       fetchJobs(); // Refresh the job list with final status
//     } catch (error) {
//       console.error("Error submitting job:", error);
//     }
//   };

//   return (
//     <div className="container my-3">
//       <form onSubmit={handleSubmit}>
//         <label htmlFor="menu">Choose an option:</label>
//         <select
//           id="menu"
//           name="menu"
//           onChange={handleChange}
//           className="form-select"
//           required
//         >
//           <option value="">Select</option>
//           <option value="tes2s.py" id="1">
//             File 1
//           </option>
//           <option value="tes3s.py" id="2">
//             File 2
//           </option>
//         </select>
//         <button type="submit" className="btn btn-primary mt-2">
//           Run
//         </button>
//       </form>
//     </div>
//   );
// };

// DropdownForm.propTypes = {
//   fetchJobs: PropTypes.func.isRequired,
// };

// export default DropdownForm;
// #######################################################################################################################

import { useState } from "react";
import axios from "axios";
import PropTypes from "prop-types";

const DropdownForm = ({ fetchJobs }) => {
  const [menu, setMenu] = useState("");
  const [optionId, setOptionId] = useState("");
  const [optionText, setOptionText] = useState("");

  const handleChange = (e) => {
    const selectedOption = e.target.options[e.target.selectedIndex];
    setMenu(e.target.value);
    setOptionId(selectedOption.id);
    setOptionText(selectedOption.text);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Temporary "In Progress" Job
    const inProgressJob = {
      id: Date.now(), // Temporary ID
      job_id: optionId,
      playbook: optionText,
      date: new Date().toISOString().split("T")[0],
      start_time: new Date().toLocaleTimeString(),
      end_time: "--",
      duration: "--",
      status: "In Progress",
    };

    fetchJobs((prevJobs) => [inProgressJob, ...prevJobs]); // Add "In Progress" to the list

    try {
      const response = await axios.post("http://192.168.1.25:8000/", {
        menu,
        option_id: optionId,
        option_text: optionText,
      });

      console.log("Job Submitted:", response.data);
      fetchJobs(response.data.jobs); // Update with backend data
    } catch (error) {
      console.error("Error submitting job:", error);
      alert("Failed to submit the job. Check the server connection.");
    }
  };

  return (
    <div className="container my-3">
      <form onSubmit={handleSubmit}>
        <label htmlFor="menu">Choose an option:</label>
        <select
          id="menu"
          name="menu"
          onChange={handleChange}
          className="form-select"
          required
        >
          <option value="">Select</option>
          <option value="tes2s.yaml" id="1">
            File 1
          </option>
          <option value="tes3s.py" id="2">
            File 2
          </option>
        </select>
        <button type="submit" className="btn btn-primary mt-2">
          Run
        </button>
      </form>
    </div>
  );
};

DropdownForm.propTypes = {
  fetchJobs: PropTypes.func.isRequired,
};

export default DropdownForm;
