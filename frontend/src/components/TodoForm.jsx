// import { useState } from "react";
// import PropTypes from "prop-types";

// const TodoForm = ({ addTodo }) => {
//   const [title, setTitle] = useState("");
//   const [desc, setDesc] = useState("");

// const handleSubmit = (e) => {
//   e.preventDefault();
//   addTodo({ title, desc, date_created: new Date().toLocaleString() });
//   setTitle("");
//   setDesc("");
// };

//   return (
//     <div className="container my-3">
//       <form onSubmit={handleSubmit}>
//         <label>Todo Title</label>
//         <input
//           type="text"
//           className="form-control"
//           value={title}
//           onChange={(e) => setTitle(e.target.value)}
//         />
//         <label>Todo Description</label>
//         <input
//           type="text"
//           className="form-control"
//           value={desc}
//           onChange={(e) => setDesc(e.target.value)}
//         />
//         <button type="submit" className="btn btn-primary mt-2">
//           Submit
//         </button>
//       </form>
//     </div>
//   );
// };
// };

// TodoForm.propTypes = {
//   addTodo: PropTypes.func.isRequired,
// };

// export default TodoForm;
