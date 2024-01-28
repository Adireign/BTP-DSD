import React from 'react'
import { useLocation } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import { useSearchParams } from 'react-router-dom'
import jsPDF from 'jspdf';
import { useState } from 'react';


const AssessmentDone = () => {
    const navigate = useNavigate()
    const { questions, marks } = useLocation().state
    const marksScored = marks[0]
    const totalMarks = marks[1]
    const seconds = marks[2]
    const percentage = (marksScored / totalMarks) * 100
    const handleClick1 = () => {
        console.log(questions)
        console.log(marks)
    }
    const handleClick2 = () => {
        navigate('/')
    }
    const generatePDF = () => {
        const pdf = new jsPDF();
        let yOffset = 20; // Initial y offset
        const xOffset = 20; // Left margin
        const lines = pdf.splitTextToSize(`Questions and answers`, pdf.internal.pageSize.width - xOffset);
        pdf.text(xOffset+50, yOffset, lines);
        yOffset += 20;

        questions.forEach((q, index) => {
          // Check if adding a new question exceeds the page height
          const pageHeight = pdf.internal.pageSize.height;
          const lineHeight = 10; // Adjust as needed
          const spaceNeeded = lineHeight * (q.options.length + 3); // Question + Options + Correct Answer
          if (yOffset + spaceNeeded > pageHeight) {
            pdf.addPage(); // Move to a new page
            yOffset = 10; // Reset the y offset
          }
    
          // Add question with left margin
          const lines = pdf.splitTextToSize(`Q ${index + 1}: ${q.question}`, pdf.internal.pageSize.width - xOffset);
          pdf.text(xOffset, yOffset, lines);
          yOffset += lineHeight * lines.length;
    
          // Add options with left margin
          q.options.forEach((option, optionIndex) => {
            const optionLines = pdf.splitTextToSize(`${option}`, pdf.internal.pageSize.width - xOffset - 10);
            pdf.text(xOffset + 10, yOffset, optionLines);
            yOffset += lineHeight * optionLines.length;
          });
    
          // Add correct answer with left margin
          const answerLines = pdf.splitTextToSize(`Correct Answer: ${q.answer}`, pdf.internal.pageSize.width - xOffset - 10);
          pdf.text(xOffset + 10, yOffset, answerLines);
          yOffset += lineHeight * answerLines.length;
    
          // Add extra space between questions
          yOffset += lineHeight;
        });
    
        // Save the PDF
        pdf.save('questions.pdf');
      };
    return (
        <div>
            <div class="bg-white py-24 sm:py-32">
                <div class="mx-auto max-w-7xl px-6 lg:px-8">
                    <dl class="grid grid-cols-1 gap-x-8 gap-y-16 text-center lg:grid-cols-4">
                        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
                            <dt class="text-base leading-7 text-gray-600">Total questions</dt>
                            <dd class="order-first text-3xl font-semibold tracking-tight text-gray-900 sm:text-5xl">{totalMarks}</dd>
                        </div>
                        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
                            <dt class="text-base leading-7 text-gray-600">Questions solved correctly</dt>
                            <dd class="order-first text-3xl font-semibold tracking-tight text-gray-900 sm:text-5xl">{marksScored}</dd>
                        </div>
                        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
                            <dt class="text-base leading-7 text-gray-600">Percentage secured</dt>
                            <dd class="order-first text-3xl font-semibold tracking-tight text-gray-900 sm:text-5xl">{percentage}%</dd>
                        </div>
                        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
                            <dt class="text-base leading-7 text-gray-600">Time taken</dt>
                            <dd class="order-first text-3xl font-semibold tracking-tight text-gray-900 sm:text-5xl">{seconds}s</dd>
                        </div>
                    </dl>
                </div>
                <br />
                <div class="mt-10 flex items-center justify-center gap-x-6">
                    <a onClick={generatePDF} class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Download complete PDF with answers</a>
                    <button onClick={handleClick2} class="text-sm font-semibold leading-6 text-gray-900">Attempt another quiz<span aria-hidden="true">→</span></button>
                </div>
                {/* <button onClick={generatePDF}>Download PDF</button> */}
            </div>
        </div>
    )
}

export default AssessmentDone
