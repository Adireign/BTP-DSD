import React, { useState, useRef } from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const questionsData = [
  {
    question: 'What is the capital of France?',
    options: ['Berlin', 'London', 'Paris', 'Madrid'],
  },
  {
    question: 'Which programming language is this code written in?',
    options: ['Java', 'Python', 'JavaScript', 'C++'],
  },
  // Add more questions as needed
];

const Carousel = () => {
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [feedback1, setFeedback1] = useState({});
  const [feedback2, setFeedback2] = useState({});
  const [feedback3, setFeedback3] = useState({});
  const [feedback4, setFeedback4] = useState({});
  const sliderRef = useRef(null);
  const completeFeedback = {
    selectedOptions: {},
    feedback1: {},
    feedback2: {},
    feedback3: {},
    feedback4: {},
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
    console.log(completeFeedback)
    try {
      const response = await fetch("http://localhost:5000/submit_assessment",{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',

        },
        body: JSON.stringify(completeFeedback)
      })
      const data = await response.json()
      console.log(data)
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
      <Slider ref={sliderRef} {...settings}>
        {questionsData.map((questionObj, questionIndex) => (
          <div key={questionIndex} className="bg-gray-200 p-4 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">{questionObj.question}</h2>
            <ul>
              {questionObj.options.map((option, optionIndex) => (
                <li
                  key={optionIndex}
                  className={`list-disc ml-4 ${selectedOptions[questionIndex] === optionIndex
                    ? 'text-blue-500 font-bold'
                    : ''
                    }`}
                  onClick={() => handleOptionSelect(questionIndex, optionIndex)}
                >
                  {option}
                </li>
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

            <div className="mt-20">
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
          </div>
        ))}
      </Slider>
      <button
        className="mb-5 ml-5 mr-5 bg-blue-500 text-white px-4 py-2 mt-4 rounded"
        onClick={handleSubmit}
      >
        Submit Quiz
      </button>
      <br/>
    </div>
  );
};

export default Carousel;
