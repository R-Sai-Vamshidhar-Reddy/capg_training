
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// Simple components
const Home = () => <h2>Home Page</h2>;
const About = () => <h2>About Page</h2>;

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;

// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link, Outlet } from "react-router-dom";

// const Home = () => <h2>Home Page</h2>;
// const Dashboard = () => (
//   <div>
//     <h2>Dashboard</h2>
//     <nav>
//       <ul>
//         <li><Link to="profile">Profile</Link></li>
//         <li><Link to="settings">Settings</Link></li>
//       </ul>
//     </nav>
//     <Outlet />
//   </div>
// );

// const Profile = () => <h3>Profile Page</h3>;
// const Settings = () => <h3>Settings Page</h3>;

// function App() {
//   return (
//     <Router>
//       <nav>
//         <ul>
//           <li><Link to="/">Home</Link></li>
//           <li><Link to="/dashboard">Dashboard</Link></li>
//         </ul>
//       </nav>

//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/dashboard" element={<Dashboard />}>
//           <Route path="profile" element={<Profile />} />
//           <Route path="settings" element={<Settings />} />
//         </Route>
//       </Routes>
//     </Router>
//   );
// }

// export default App;
// ```

// ---

// ## 4. Redirect and Not Found Page
// This example demonstrates:
// - Redirecting users to another page using `<Navigate />`
// - Handling **404 Not Found** pages.

// ### Code:
// #### `App.js`
// ```jsx
// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";

// const Home = () => <h2>Home Page</h2>;
// const About = () => <h2>About Page</h2>;
// const NotFound = () => <h2>404 - Page Not Found</h2>;

// function App() {
//   return (
//     <Router>
//       <nav>
//         <ul>
//           <li><Link to="/">Home</Link></li>
//           <li><Link to="/about">About</Link></li>
//         </ul>
//       </nav>

//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/about" element={<About />} />
//         <Route path="/old-about" element={<Navigate to="/about" />} />
//         <Route path="*" element={<NotFound />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;
// ```

// ---

// ## 5. Protected Routes Example
// This example shows how to **protect routes** using authentication.

// ### Steps:
// 1. Create a **ProtectedRoute** component.
// 2. If the user is **not logged in**, redirect them to `/login`.

// ### Code:
// #### `ProtectedRoute.js`
// ```jsx
// import React from "react";
// import { Navigate } from "react-router-dom";

// const ProtectedRoute = ({ children }) => {
//   const isAuthenticated = false; // Change to true to allow access
//   return isAuthenticated ? children : <Navigate to="/login" />;
// };

// export default ProtectedRoute;
// ```

// #### `App.js`
// ```jsx
// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// import ProtectedRoute from "./ProtectedRoute";

// const Home = () => <h2>Home Page</h2>;
// const Dashboard = () => <h2>Dashboard - Protected</h2>;
// const Login = () => <h2>Login Page</h2>;

// function App() {
//   return (
//     <Router>
//       <nav>
//         <ul>
//           <li><Link to="/">Home</Link></li>
//           <li><Link to="/dashboard">Dashboard</Link></li>
//           <li><Link to="/login">Login</Link></li>
//         </ul>
//       </nav>

//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/login" element={<Login />} />
//         <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;