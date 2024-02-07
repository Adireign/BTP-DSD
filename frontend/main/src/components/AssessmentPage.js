import React, { useState, useRef } from 'react';
import { useEffect } from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { useLocation, useNavigate } from 'react-router-dom';
import AssessmentDone from './AssessmentDone';

// const questionsData = [
//   {
//     question: 'What is the capital of France?',
//     options: ['A. Berlin', 'B. London', 'C. Paris', 'D. Madrid'],
//     answer: ['A. Berlin']
//   },
//   {
//     question: 'Which programming language is this code written in?',
//     options: ['A. Java', 'B. Python', 'C. JavaScript', 'D. C++'],
//     answer: ['C. JavaScript']
//   },
//   // Add more questions as needed
// ];

const Carousel = () => {
  const navigate = useNavigate()
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

  useEffect(() => {
    const fetchQuestionData = async () => {
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
      if (questionsData[i].answer[0][0] == 'A') {
        completeFeedback.correctOptions[key] = "0"
      }
      else if (questionsData[i].answer[0][0] == 'B') {
        completeFeedback.correctOptions[key] = "1"
      }
      else if (questionsData[i].answer[0][0] == 'C') {
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

  return (
    <div>
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
              <div className='feeback1'>
                <p className="mb-2">Was the question helpful?</p>
                <label className="mr-4">
                  <input
                    type="radio"
                    name={`feedback1_${questionIndex}`}
                    value="helpful"
                    onChange={() => handleFeedbackChange1(questionIndex, 'helpful')}
                  />
                  Helpful
                </label>
                <label className="mr-4">
                  <input
                    type="radio"
                    name={`feedback1_${questionIndex}`}
                    value="not_helpful"
                    onChange={() =>
                      handleFeedbackChange1(questionIndex, 'not_helpful')
                    }
                  />
                  Not Helpful
                </label>
              </div>
              <div className='feedback2'>
                <p className="mt-4 mb-2">Was the question Ambiguous?</p>
                <label className="mr-4">
                  <input
                    type="radio"
                    name={`feedback2_${questionIndex}`}
                    value="Ambiguous"
                    onChange={() => handleFeedbackChange2(questionIndex, 'Ambiguous')}
                  />
                  Ambiguous
                </label>
                <label className="mr-4">
                  <input
                    type="radio"
                    name={`feedback2_${questionIndex}`}
                    value="not_Ambiguous"
                    onChange={() =>
                      handleFeedbackChange2(questionIndex, 'not_Ambiguous')
                    }
                  />
                  Not Ambiguous
                </label>
              </div>

              <p className="mt-4 mb-2">Were choices easy to eliminate?</p>
              <label className="mr-4">
                <input
                  type="radio"
                  name={`feedback3_${questionIndex}`}
                  value="easy_to_eliminate"
                  onChange={() => handleFeedbackChange3(questionIndex, 'easy_to_eliminate')}
                />
                easy to eliminate
              </label>
              <label className="mr-4">
                <input
                  type="radio"
                  name={`feedback3_${questionIndex}`}
                  value="not_easy_to_eliminate"
                  onChange={() =>
                    handleFeedbackChange3(questionIndex, 'not_easy_to_eliminate')
                  }
                />
                Not easy to eliminate
              </label>
              <p className="mt-4 mb-2">Was the question Lengthy?</p>
              <label className="mr-4">
                <input
                  type="radio"
                  name={`feedback4_${questionIndex}`}
                  value="lenghty"
                  onChange={() => handleFeedbackChange4(questionIndex, 'lenghty')}
                />
                Lenghty
              </label>
              <label className="mr-4">
                <input
                  type="radio"
                  name={`feedback4_${questionIndex}`}
                  value="not_lenghty"
                  onChange={() =>
                    handleFeedbackChange4(questionIndex, 'not_lenghty')
                  }
                />
                Not lenghty
              </label>
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
