import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import ChatbotPage from "./pages/ChatbotPage/ChatbotPage";

function App() {

  return (

    <BrowserRouter>

      <Routes>



        <Route
          path="/"
          element={<ChatbotPage />}
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;