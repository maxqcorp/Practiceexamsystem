import { createBrowserRouter, Outlet } from "react-router-dom";
import Login from "./components/Login";
import Landing from "./components/Landing";
import FiftyQuestionSets from "./components/FiftyQuestionSets";
import Exam from "./components/Exam";
import QuickPractice from "./components/QuickPractice";
import QuickExam from "./components/QuickExam";
import RamDSets from "./components/RamDSets";
import RamDExam from "./components/RamDExam";
import DavidYTSets from "./components/DavidYTSets";
import DavidYTExam from "./components/DavidYTExam";
import ReviewExam from "./components/ReviewExam";
import PMPSimulation from "./components/pmp/PMPSimulation";
import PMPExam from "./components/pmp/PMPExam";
import ReleaseNotes from "./components/ReleaseNotes";
import ProtectedRoute from "./components/ProtectedRoute";
import { AuthProvider } from "./contexts/AuthContext";

function RootLayout() {
  return (
    <AuthProvider>
      <Outlet />
    </AuthProvider>
  );
}

export const router = createBrowserRouter([
  {
    element: <RootLayout />,
    children: [
      {
        path: "/login",
        Component: Login,
      },
      {
        path: "/",
        element: <ProtectedRoute><Landing /></ProtectedRoute>,
      },
      {
        path: "/sets-50",
        element: <ProtectedRoute><FiftyQuestionSets /></ProtectedRoute>,
      },
      {
        path: "/exam/:setId",
        element: <ProtectedRoute><Exam /></ProtectedRoute>,
      },
      {
        path: "/sets-25",
        element: <ProtectedRoute><QuickPractice /></ProtectedRoute>,
      },
      {
        path: "/quick-practice/:setId",
        element: <ProtectedRoute><QuickExam /></ProtectedRoute>,
      },
      {
        path: "/sets-ramd",
        element: <ProtectedRoute><RamDSets /></ProtectedRoute>,
      },
      {
        path: "/ramd/:setId",
        element: <ProtectedRoute><RamDExam /></ProtectedRoute>,
      },
      {
        path: "/sets-davidyt",
        element: <ProtectedRoute><DavidYTSets /></ProtectedRoute>,
      },
      {
        path: "/davidyt/:setId",
        element: <ProtectedRoute><DavidYTExam /></ProtectedRoute>,
      },
      {
        path: "/review/:source",
        element: <ProtectedRoute><ReviewExam /></ProtectedRoute>,
      },
      {
        path: "/pmp-simulation",
        element: <ProtectedRoute><PMPSimulation /></ProtectedRoute>,
      },
      {
        path: "/pmp-exam/:mode",
        element: <ProtectedRoute><PMPExam /></ProtectedRoute>,
      },
      {
        path: "/release-notes",
        element: <ProtectedRoute><ReleaseNotes /></ProtectedRoute>,
      },
    ],
  },
]);