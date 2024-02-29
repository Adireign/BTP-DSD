import React, { useState, useRef } from 'react';
import { useEffect } from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { useLocation, useNavigate } from 'react-router-dom';
import AssessmentDone from './AssessmentDone';
import "./test.css"
import LoadingAssessment from './LoadingAssessment';

const emojis = ['😍', '😂', '😲', '😢', '😡'];


const Carousel = () => {
  const navigate = useNavigate()
  const [loading, setLoading] = useState(true)
  const [selectedData, setSelectedData] = useState(null);
  const [questionsData, setQuestionsData] = useState([])
  const { numQuestions, selectedTags, selectedLevel } = useLocation().state;
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [feedback1, setFeedback1] = useState({});
  const [feedback2, setFeedback2] = useState({});
  const [feedback3, setFeedback3] = useState({});
  const [feedback4, setFeedback4] = useState({});
  const [seconds, setSeconds] = useState(0);
  const sliderRef = useRef(null);
  const completeFeedback = {
    selectedOptions: {},
    correctOptions: {},
    feedback1: {},
    feedback2: {},
    feedback3: {},
    feedback4: {},
  }
  const [isHovering1, setIsHovering1] = useState(false);
  const [isHovering2, setIsHovering2] = useState(false);
  const [isHovering3, setIsHovering3] = useState(false);
  const [isHovering4, setIsHovering4] = useState(false);

  const handleMouseEnter1 = () => {
    setIsHovering1(true);
  };

  const handleMouseLeave1 = () => {
    setIsHovering1(false);
  };

  const handleMouseEnter2 = () => {
    setIsHovering2(true);
  };

  const handleMouseLeave2 = () => {
    setIsHovering2(false);
  };

  const handleMouseEnter3 = () => {
    setIsHovering3(true);
  };

  const handleMouseLeave3 = () => {
    setIsHovering3(false);
  };

  const handleMouseEnter4 = () => {
    setIsHovering4(true);
  };

  const handleMouseLeave4 = () => {
    setIsHovering4(false);
  };


  const [answeredQuestions, setAnsweredQuestions] = useState([]);
  const [numberOfQuestions, setNumberOfQuestions] = useState(0);



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
    setSelectedOptions((prevSelectedOptions) => ({
      ...prevSelectedOptions,
      [questionIndex]: optionIndex,
    }));
  };

  const handleFeedbackChange1 = (questionIndex, feedbackType) => {
    setFeedback1((prevFeedback) => ({
      ...prevFeedback,
      [questionIndex]: feedbackType,
    }));
  };
  const handleFeedbackChange2 = (questionIndex, feedbackType) => {
    setFeedback2((prevFeedback) => ({
      ...prevFeedback,
      [questionIndex]: feedbackType,
    }));
  };
  const handleFeedbackChange3 = (questionIndex, feedbackType) => {
    setFeedback3((prevFeedback) => ({
      ...prevFeedback,
      [questionIndex]: feedbackType,
    }));
  };
  const handleFeedbackChange4 = (questionIndex, feedbackType) => {
    setFeedback4((prevFeedback) => ({
      ...prevFeedback,
      [questionIndex]: feedbackType,
    }));
  };

  const handleSubmit = async () => {
    completeFeedback.selectedOptions = selectedOptions
    completeFeedback.feedback1 = feedback1
    completeFeedback.feedback2 = feedback2
    completeFeedback.feedback3 = feedback3
    completeFeedback.feedback4 = feedback4
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
      const data = await response.json()
      console.log(data)
      const marksScored = data.marks_scored
      const totalMarks = data.total_marks
      const marks = [marksScored, totalMarks, seconds]
      navigate('/AssessmentDone', { state: { questions: questionsData, marks } });
    } catch (error) {
      console.log(error)
    }
  };

  const handleNext = () => {
    sliderRef.current.slickNext();
  };

  const handlePrev = () => {
    sliderRef.current.slickPrev();
  };

  const settings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };
  const handleAnswerQuestion = (questionId) => {
    // Mark the question as answered
    setAnsweredQuestions([...answeredQuestions, questionId]);
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

            <div style={styles.container}>
              <p style={styles.timerText}>Timer: {seconds} seconds</p>
            </div>
            <Slider className='p-4' ref={sliderRef} {...settings}>
              {questionsData.map((questionObj, questionIndex) => (
                <>
                  <div key={questionIndex} className="bg-gray-200 p-4 rounded shadow">
                    <h2 className="text-2xl font-bold mb-4">{questionObj.question}</h2>
                    <ul>
                      {questionObj.options.map((option, optionIndex) => (
                        <div
                          key={optionIndex}
                          className={`list-disc ml-4 ${selectedOptions[questionIndex] === optionIndex
                            ? 'text-blue-500 font-bold'
                            : ''
                            }`}
                          onClick={() => handleOptionSelect(questionIndex, optionIndex)}
                        >
                          {option}
                        </div>
                      ))}
                    </ul>
                    <div className="ml-5 mr-5 mt-4 flex justify-between">
                      <button
                        className="bg-blue-500 text-white px-4 py-2 rounded"
                        onClick={handlePrev}
                      >
                        Previous
                      </button>
                      <button
                        className="bg-blue-500 text-white px-4 py-2 rounded"
                        onClick={handleNext}
                      >
                        Next
                      </button>
                    </div>


                  </div>
                  <div className="mt-20 pl-2">
                    <b>Feedback</b>
                    {/* Feedback-1 */}
                    <div className="border border-gray-200 rounded-lg shadow-md p-4 relative hover:shadow-lg transition duration-300" onMouseEnter={handleMouseEnter1} onMouseLeave={handleMouseLeave1}>
                      <div className="mb-4 text-gray-800">
                        Was this question Helpful?
                      </div>

                      {isHovering1 && (
                        <div className="absolute bottom-0 right-0 flex space-x-2">
                          {emojis.map((emoji, index) => (
                            <span key={index} onClick={() => handleFeedbackChange1(questionIndex, emoji)} className="cursor-pointer text-xl">
                              {emoji}
                            </span>
                          ))}
                        </div>
                      )}

                      {feedback1 && (
                        <div className="mt-2 text-lg text-gray-700 font-medium">
                          You selected: {feedback1[questionIndex]}
                        </div>
                      )}
                    </div>

                    <div className="border border-gray-200 rounded-lg shadow-md p-4 relative hover:shadow-lg transition duration-300" onMouseEnter={handleMouseEnter2} onMouseLeave={handleMouseLeave2}>
                      <div className="mb-4 text-gray-800">
                        Was the question ambiguous?
                      </div>

                      {isHovering2 && (
                        <div className="absolute bottom-0 right-0 flex space-x-2">
                          {emojis.map((emoji, index) => (
                            <span key={index} onClick={() => handleFeedbackChange2(questionIndex, emoji)} className="cursor-pointer text-xl">
                              {emoji}
                            </span>
                          ))}
                        </div>
                      )}

                      {feedback2 && (
                        <div className="mt-2 text-lg text-gray-700 font-medium">
                          You selected: {feedback2[questionIndex]}
                        </div>
                      )}
                    </div>

                    <div className="border border-gray-200 rounded-lg shadow-md p-4 relative hover:shadow-lg transition duration-300" onMouseEnter={handleMouseEnter3} onMouseLeave={handleMouseLeave3}>
                      <div className="mb-4 text-gray-800">
                        Was the question lengthy?
                      </div>

                      {isHovering3 && (
                        <div className="absolute bottom-0 right-0 flex space-x-2">
                          {emojis.map((emoji, index) => (
                            <span key={index} onClick={() => handleFeedbackChange3(questionIndex, emoji)} className="cursor-pointer text-xl">
                              {emoji}
                            </span>
                          ))}
                        </div>
                      )}

                      {feedback3 && (
                        <div className="mt-2 text-lg text-gray-700 font-medium">
                          You selected: {feedback3[questionIndex]}
                        </div>
                      )}
                    </div>

                    <div className="border border-gray-200 rounded-lg shadow-md p-4 relative hover:shadow-lg transition duration-300" onMouseEnter={handleMouseEnter4} onMouseLeave={handleMouseLeave4}>
                      <div className="mb-4 text-gray-800">
                        Were choices easy to eliminate?
                      </div>

                      {isHovering4 && (
                        <div className="absolute bottom-0 right-0 flex space-x-2">
                          {emojis.map((emoji, index) => (
                            <span key={index} onClick={() => handleFeedbackChange4(questionIndex, emoji)} className="cursor-pointer text-xl">
                              {emoji}
                            </span>
                          ))}
                        </div>
                      )}

                      {feedback4 && (
                        <div className="mt-2 text-lg text-gray-700 font-medium">
                          You selected: {feedback4[questionIndex]}
                        </div>
                      )}
                    </div>

                  </div>
                </>
              ))}
            </Slider>
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
