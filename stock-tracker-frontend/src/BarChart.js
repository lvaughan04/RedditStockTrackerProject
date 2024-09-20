// src/BarChart.js
import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

// Register necessary components
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const BarChart = ({ data }) => {
  // Prepare data for Chart.js
  const chartData = {
    labels: data.map(stock => stock.name), // Stock names on y-axis
    datasets: [
      {
        label: 'Mentions',
        data: data.map(stock => stock.mentions), // Mentions on x-axis
        backgroundColor: 'rgba(75, 192, 192, 0.6)', // Updated color for better contrast
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  // Configure chart options
  const options = {
    responsive: true,
    indexAxis: 'y', // Flip the axes (mentions on x-axis, stocks on y-axis)
    plugins: {
      legend: {
        position: 'top',
      },
      tooltip: {
        callbacks: {
          label: function (tooltipItem) {
            return `Mentions: ${tooltipItem.raw}`;
          },
        },
      },
    },
    scales: {
      x: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Mentions',
        },
        ticks: {
          stepSize: 10, // Adjust based on data range
        },
      },
      y: {
        title: {
          display: true,
          text: 'Stocks',
        },
        ticks: {
          autoSkip: false, // Ensures all stock names are shown even with 50 items
        },
      },
    },
    barThickness: 10, // Thinner bars to fit up to 50 stocks
    maxBarThickness: 12,
  };

  return (
    <div>
      <Bar data={chartData} options={options} />
    </div>
  );
};

export default BarChart;