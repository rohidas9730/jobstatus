import PropTypes from "prop-types";
import "../css/JobTable.css";
// const JobTable = ({ jobs }) => {
//   return (
//     <div className="container my-3">
//       <h2>Job Statuses</h2>
//       <table className="table">
//         <thead>
//           <tr>
//             <th>Job ID</th>
//             <th>File Name</th>
//             <th>Date</th>
//             <th>Start Time</th>
//             <th>End Time</th>
//             <th>Duration</th>
//             <th>Status</th>
//           </tr>
//         </thead>
//         <tbody>
//           {jobs.map((job) => (
//             <tr key={job.job_id}>
//               <td>{job.job_id}</td>
//               <td>{job.playbook}</td>
//               <td>{job.date}</td>
//               <td>{job.start_time}</td>
//               <td>{job.end_time}</td>
//               <td>{job.duration}</td>
//               <td>{job.status}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// import React from "react";

// const JobTable = ({ jobs }) => {
//   return (
//     <div className="job-table-container">
//       <h3>Job Status List</h3>
//       <table className="job-table">
//         <thead>
//           <tr>
//             <th>ID</th>
//             <th>Playbook</th>
//             <th>Date</th>
//             <th>Start Time</th>
//             <th>End Time</th>
//             <th>Duration (s)</th>
//             <th>Status</th>
//           </tr>
//         </thead>
//         <tbody>
//           {jobs.map((job) => (
//             <tr key={job.id}>
//               <td>{job.job_id}</td>
//               <td>{job.playbook}</td>
//               <td>{job.date}</td>
//               <td>{job.start_time}</td>
//               <td>{job.end_time}</td>
//               <td>{job.duration}</td>
//               <td
//                 className={
//                   job.status === "Success"
//                     ? "status-success"
//                     : job.status === "Failure"
//                     ? "status-failure"
//                     : "status-in-progress"
//                 }
//               >
//                 {job.status}
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// // export default JobList;

// // ✅ Correct placement of propTypes
// JobTable.propTypes = {
//   jobs: PropTypes.arrayOf(
//     PropTypes.shape({
//       job_id: PropTypes.string.isRequired,
//       playbook: PropTypes.string.isRequired,
//       date: PropTypes.string.isRequired,
//       start_time: PropTypes.string.isRequired,
//       end_time: PropTypes.string.isRequired,
//       duration: PropTypes.string.isRequired,
//       status: PropTypes.string.isRequired,
//     })
//   ).isRequired,
// };

// export default JobTable;

const JobTable = ({ jobs }) => {
  return (
    <div className="job-table-container">
      <h3>Job Status List is below</h3>
      <table className="job-table table table-bordered table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Playbook</th>
            <th>Date</th>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Duration</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((job) => (
            <tr
              key={job.id}
              className={
                job.status === "In Progress"
                  ? "table-warning"
                  : job.status === "Success"
                  ? "table-success"
                  : "table-danger"
              }
            >
              <td>{job.job_id}</td>
              <td>{job.playbook}</td>
              <td>{job.date}</td>
              <td>{job.start_time}</td>
              <td>{job.end_time}</td>
              <td>{job.duration}</td>
              <td>{job.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

JobTable.propTypes = {
  jobs: PropTypes.arrayOf(
    PropTypes.shape({
      job_id: PropTypes.string.isRequired,
      playbook: PropTypes.string.isRequired,
      date: PropTypes.string.isRequired,
      start_time: PropTypes.string.isRequired,
      end_time: PropTypes.string.isRequired,
      duration: PropTypes.string.isRequired,
      status: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default JobTable;
