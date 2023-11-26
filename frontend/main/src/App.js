import UpperNav from "./components/UpperNav";
import TagSelection from "./components/TagSelection";
import LevelSelector from "./components/LevelSelection";
import QuestionInput from "./components/QuestionInput";
import QuizForm from "./components/Form";

function App() {
  const tags = ['tag1', 'tag2', 'tag3', 'tag4'];
  return (
    <div className="App">
      <UpperNav/>
      {/* <TagSelection availableTags={tags}/> */}
      {/* <LevelSelector/> */}
      {/* <QuestionInput/> */}
      <QuizForm/>
      
    </div>
  );
}

export default App;
