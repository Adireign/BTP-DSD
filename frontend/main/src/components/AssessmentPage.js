import React, { useState, useRef } from 'react';
import { useEffect } from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { useLocation, useNavigate } from 'react-router-dom';
import AssessmentDone from './AssessmentDone';
// import "./test.css"
import LoadingAssessment from './LoadingAssessment';
import UpperNav from './UpperNav';

const emojis = ['😍', '😂', '😲', '😢', '😡'];


const Carousel = () => {
  const navigate = useNavigate()
  const [loading, setLoading] = useState(true)
  const [selectedData, setSelectedData] = useState(null);
  const [questionsData, setQuestionsData] = useState([])
  const {numQuestions, selectedTags, selectedLevel, loggedInName, loggedInEmail, loggedInType } = useLocation().state;
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [feedback1, setFeedback1] = useState({});
  const [seconds, setSeconds] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState(0); // Current question index
  const sliderRef = useRef(null);

  const completeFeedback = {
    selectedOptions: {},
    correctOptions: {},
    feedback1: {},
    name: {},
    email: {},
    type: 'student',
    questionBodies: {},
  }
  const [isHovering1, setIsHovering1] = useState(false);

  const handleMouseEnter1 = () => {
    setIsHovering1(true);
  };

  const handleMouseLeave1 = () => {
    setIsHovering1(false);
  };

  useEffect(() => {
    const fetchQuestionData = async () => {
      setInterval(() => {
        setLoading(false)
      }, 2000)
      const payload = {
        tags: selectedTags,
        level: selectedLevel,
        numQuestions: numQuestions,
      };
      try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/startAssessment`, {
          method: 'POST',
          headers: {
            'content-type': 'application/json',
          },
          body: JSON.stringify(payload),
        })
        const data = await response.json()
        setQuestionsData(data.questions)
        console.log('data is', data)
        const intervalId = setInterval(() => {
          setSeconds((prevSeconds) => prevSeconds + 1)
        }, 1000)
        return () => clearInterval(intervalId);
      } catch (error) {
        console.log(error)
      }
    }
    fetchQuestionData()
  }, [])
  if (!Array.isArray(questionsData)) {
    console.error('questionsData is not an array:', questionsData);
    return null; // or handle the error in another way
  }



  const handleOptionSelect = (questionIndex, optionIndex) => {
    const newSelectedOptions = [...selectedOptions];
    newSelectedOptions[questionIndex] = optionIndex;
    setSelectedOptions(newSelectedOptions);
  };

  const handleFeedbackChange1 = (questionIndex, feedbackType) => {
    setFeedback1((prevFeedback) => ({
      ...prevFeedback,
      [questionIndex]: feedbackType,
    }));
  };

  const handleSubmit = async () => {
    completeFeedback.selectedOptions = selectedOptions
    completeFeedback.feedback1 = feedback1
    completeFeedback.name = loggedInName
    completeFeedback.email = loggedInEmail
    completeFeedback.type = loggedInType
    completeFeedback.questionBodies = questionsData

    for (let i = 0; i < Object.keys(selectedOptions).length; i++) {
      let key = i.toString()
      if (questionsData[i].answer[0][0] === 'A') {
        completeFeedback.correctOptions[key] = "0"
      }
      else if (questionsData[i].answer[0][0] === 'B') {
        completeFeedback.correctOptions[key] = "1"
      }
      else if (questionsData[i].answer[0][0] === 'C') {
        completeFeedback.correctOptions[key] = "2"
      }
      else {
        completeFeedback.correctOptions[key] = "3"
      }
    }

    console.log(completeFeedback)
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/submit_assessment`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(completeFeedback)
      })
      console.log(loggedInType)
      const data = await response.json()
      console.log(data)
      const marksScored = data.marks_scored
      const totalMarks = data.total_marks
      const marks = [marksScored, totalMarks, seconds]
      navigate('/AssessmentDone', { state: { questions: questionsData, marks, loggedInName, loggedInEmail } });
    } catch (error) {
      console.log(error)
    }
  };

  const handlePrev = () => {
    setCurrentQuestion((prevQuestion) => Math.max(0, prevQuestion - 1));
  };

  const handleNext = () => {
    setCurrentQuestion((prevQuestion) => Math.min(questionsData.length - 1, prevQuestion + 1));
  };
  const handleDirectNavigation = (questionIndex) => {
    setCurrentQuestion(questionIndex);
  };

  const settings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };
  const QuestionBox = ({ questionNumber, isAnswered, onClick }) => (
    <div
      className={`question-box ${isAnswered ? 'answered' : ''}`}
      onClick={onClick}
    >
      {questionNumber}
    </div>
  );

  return (
    <div>
      {
        loading ?
          <LoadingAssessment /> :
          <>
            <UpperNav name={loggedInName} email={loggedInEmail} />
            <div style={styles.container}>
              <p style={styles.timerText}>Timer: {seconds} seconds</p>
            </div>

            <div className="p-4">
              <div className="navigation-bar mb-4">
                {questionsData.map((_, index) => (
                  <button
                    key={index}
                    className={`nav-button ${index === currentQuestion ? 'active' : ''} ${selectedOptions[index] !== null ? 'answered' : 'unanswered'}`}
                    onClick={() => handleDirectNavigation(index)}
                    style={{
                      backgroundColor: index === currentQuestion ? '#4CAF50' : selectedOptions[index] !== null ? '#2196F3' : '#ddd',
                      color: index === currentQuestion ? 'white' : selectedOptions[index] !== null ? 'white' : 'black',
                      border: 'none',
                      borderRadius: '5px',
                      padding: '10px 20px',
                      margin: '5px',
                      cursor: 'pointer',
                      transition: 'background-color 0.3s',
                    }}
                  >
                    {`Q ${index + 1}`}
                    {selectedOptions[index] != null ? (
                      <span style={{ marginLeft: '5px' }}>✔️</span>
                    ) : (
                      <span style={{ marginLeft: '5px', color: '#FF5733' }}>❌</span> // Changing the color of the cross sign
                    )}
                  </button>
                ))}
              </div>




              {questionsData.map((questionObj, questionIndex) => (
                <div key={questionIndex} className={`bg-gray-200 p-4 rounded shadow ${questionIndex === currentQuestion ? 'block' : 'hidden'}`}>
                  <h2 className="text-2xl font-bold mb-4">Q{questionIndex + 1}: {questionObj.question}</h2>
                  <ul>
                    {questionObj.options.map((option, optionIndex) => (
                      <div
                        key={optionIndex}
                        className={`list-disc ml-4 ${selectedOptions[questionIndex] === optionIndex ? 'text-blue-500 font-bold' : ''}`}
                        onClick={() => handleOptionSelect(questionIndex, optionIndex)}
                      >
                        {option}
                      </div>
                    ))}
                  </ul>
                  <div className="mb-5 ml-5 mr-5 mt-4 flex justify-between">
                    <button
                      className="bg-blue-500 text-white px-4 py-2 rounded"
                      onClick={handlePrev}
                      disabled={currentQuestion === 0}
                    >
                      Previous
                    </button>
                    <button
                      className="bg-blue-500 text-white px-4 py-2 rounded"
                      onClick={handleNext}
                      disabled={currentQuestion === questionsData.length - 1}
                    >
                      Next
                    </button>

                  </div>
                  <div className="border border-blue-200 rounded-lg shadow-md p-4 relative hover:shadow-lg transition duration-300" style={{ width: '20%' }} onMouseEnter={handleMouseEnter1} onMouseLeave={handleMouseLeave1}>
                    <div className="mb-4 text-blue-800">
                      Rate this?

                    {isHovering1 && (
                      <div className="relative">

                        <div className="absolute bottom-0 right-0">
                          {emojis.map((emoji, index) => (
                            <span key={index} onClick={() => handleFeedbackChange1(questionIndex, emoji)} className="cursor-pointer text-xl">
                              {emoji}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                    </div>

                    {feedback1 && (
                      <div className="mt-2 text-lg text-blue-700 font-medium">
                        You selected: {feedback1[questionIndex]}
                      </div>
                    )}
                  </div>
                </div>

              ))}

            </div>
            <button
              className="mb-5 ml-5 mr-5 bg-blue-500 text-white px-4 py-2 mt-2 rounded"
              onClick={handleSubmit}
            >
              Submit Quiz
            </button>
            <br />

          </>
      }
    </div>
  );
};
const styles = {
  container: {
    textAlign: 'center',
    marginTop: '20px',
  },
  timerText: {
    fontSize: '20px',
    fontWeight: 'bold',
    color: '#333',
  },
};

export default Carousel;
