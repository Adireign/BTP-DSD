import React, { useState } from 'react';

const QuizForm = () => {
  const [selectedTags, setSelectedTags] = useState([]);
  const [selectedLevel, setSelectedLevel] = useState(null);
  const [numQuestions, setNumQuestions] = useState('');

  const handleTagClick = (tag) => {
    if (selectedTags.includes(tag)) {
      setSelectedTags(selectedTags.filter((selectedTag) => selectedTag !== tag));
    } else {
      setSelectedTags([...selectedTags, tag]);
    }
  };

  const handleLevelClick = (level) => {
    setSelectedLevel(level);
  };

  const handleInputChange = (event) => {
    const inputValue = event.target.value;
    setNumQuestions(inputValue);
  };

  const handleSubmit = async (event) => {
    console.log(selectedTags)
    console.log(selectedLevel)
    console.log(numQuestions)
    event.preventDefault();

    // Create payload to send to the server
    const payload = {
      tags: selectedTags,
      level: selectedLevel,
      numQuestions: numQuestions,
    };

    try {
      // Send POST request to the Flask server
      const response = await fetch('http://localhost:5000/submit_quiz', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      // Handle the response as needed
      if (response.ok) {
        console.log('Quiz submitted successfully!');
      } else {
        console.error('Failed to submit quiz.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const tags = ['Number-System', 'Boolean-algebra', 'Gates', 'Flip-flops', 'Theory'];
  const levels = ['Level-1', 'Level-2', 'Level-3'];

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Quiz Configuration</h2>
      <div className="space-y-4">
        {/* Tag Selector */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Select Tags</h3>
          <div className="space-x-2">
            {tags.map((tag) => (
              <span
                key={tag}
                className={`inline-block px-3 py-1 text-sm font-semibold rounded-full cursor-pointer ${
                  selectedTags.includes(tag) ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-700'
                }`}
                onClick={() => handleTagClick(tag)}
              >
                {tag}
              </span>
            ))}
          </div>
        </div>

        {/* Level Selector */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Select Level</h3>
          <div className="space-x-2">
            {levels.map((level) => (
              <span
                key={level}
                className={`inline-block px-3 py-1 text-sm font-semibold rounded-full cursor-pointer ${
                  selectedLevel === level ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-700'
                }`}
                onClick={() => handleLevelClick(level)}
              >
                {level}
              </span>
            ))}
          </div>
        </div>

        {/* Question Input */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Enter Number of Questions</h3>
          <form onSubmit={handleSubmit} className="flex items-center space-x-2">
            <label htmlFor="numQuestionsInput" className="text-gray-700">
              Questions:
            </label>
            <input
              type="number"
              id="numQuestionsInput"
              className="p-2 border rounded-md"
              value={numQuestions}
              onChange={handleInputChange}
            />
          </form>
        </div>
      </div>

      {/* Submit Button */}
      <div className="mt-4">
        <button
          onClick={handleSubmit}
          className="p-2 bg-blue-500 text-white rounded-md cursor-pointer"
        >
          Submit Quiz
        </button>
      </div>
    </div>
  );
};

export default QuizForm;
