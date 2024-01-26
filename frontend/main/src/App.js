import UpperNav from "./components/UpperNav";
import TagSelection from "./components/TagSelection";
import LevelSelector from "./components/LevelSelection";
import QuestionInput from "./components/QuestionInput";
import QuizForm from "./components/Form";
import FileList from "./components/Archives";
import Team from "./components/Team";
import Topic from "./components/Topic";
import { Route, Routes } from 'react-router-dom';
import AssessmentPage from "./components/AssessmentPage";
import AssessmentDone from "./components/AssessmentDone";


function App() {
  const tags = ['tag1', 'tag2', 'tag3', 'tag4'];
  return (
    // <div className="App">
    //   <UpperNav/>
    //   {/* <TagSelection availableTags={tags}/> */}
    //   {/* <LevelSelector/> */}
    //   {/* <QuestionInput/> */}
    //   <QuizForm/>

    // </div>
    <>
      <Routes>
        <Route path='/' index element={
          <>
            <UpperNav />
            <QuizForm />
          </>
        } />
        <Route path='/past-questions' index element={
          <>
            <UpperNav />
            <FileList />
          </>
        } />
        <Route path='/team' index element={
          <>
            <UpperNav />
            {/* <Topic/> */}
          </>
        } />
        <Route path='/AssessmentPage' index element={
          <>
            <UpperNav />
            <AssessmentPage />
          </>
        } />
        <Route path='/AssessmentDone' index element={
          <>
            <UpperNav />
            <AssessmentDone />
          </>
        } />

      </Routes>
    </>
  );
}

export default App;
