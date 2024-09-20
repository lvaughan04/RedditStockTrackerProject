import './App.css'; // Import custom styles
import React, { useState } from 'react'; // Import React hooks
import BarChart from './BarChart'; // Import the BarChart component

function App() {
  // Mock stock data with mentions and posts for each stock
  const [stocks] = useState([
    {
      symbol: 'AAPL',
      name: 'Apple Inc.',
      mentions: 12,
      posts: [
        {
          title: 'Apple stock is soaring!',
          body: 'AAPL is up due to strong sales this quarter.',
          subreddit: 'r/wallstreetbets',
          timestamp: '2024-09-16T10:15:00Z',
          author: 'user123'
        },
        {
          title: 'I think AAPL is overvalued.',
          body: 'Too much hype around the iPhone release.',
          subreddit: 'r/investing',
          timestamp: '2024-09-16T11:30:00Z',
          author: 'user456'
        }
      ]
    },
    {
      symbol: 'TSLA',
      name: 'Tesla, Inc.',
      mentions: 9,
      posts: [
        {
          title: 'Tesla just hit a new high!',
          body: 'Elon’s tweets are pushing TSLA to new highs.',
          subreddit: 'r/tesla',
          timestamp: '2024-09-16T09:00:00Z',
          author: 'user789'
        }
      ]
    },
    {
      symbol: 'AMZN',
      name: 'Amazon.com, Inc.',
      mentions: 7,
      posts: [
        {
          title: 'Amazon is up due to holiday sales.',
          body: 'Strong holiday sales are boosting AMZN.',
          subreddit: 'r/finance',
          timestamp: '2024-09-16T12:30:00Z',
          author: 'user321'
        }
      ]
    }
  ]);

  const [filter, setFilter] = useState(''); // State to store the selected filter
  const [search, setSearch] = useState(''); // State for search input
  const [filteredStocks, setFilteredStocks] = useState(stocks); // State for filtered stocks

  // Function to handle filtering and search
  const applyFilter = () => {
    let filtered = [...stocks];
    
    // Apply search filter
    if (search) {
      filtered = filtered.filter(stock => 
        stock.name.toLowerCase().includes(search.toLowerCase()) || 
        stock.posts.some(post => post.subreddit.toLowerCase().includes(search.toLowerCase()))
      );
    }
    
    // Apply sort filter
    if (filter === 'mentions') {
      filtered = filtered.sort((a, b) => b.mentions - a.mentions); // Sort by mentions (descending)
    } else if (filter === 'mentions-asc') {
      filtered = filtered.sort((a, b) => a.mentions - b.mentions); // Sort by mentions (ascending)
    } else if (filter === 'subreddit') {
      filtered = filtered.sort((a, b) => a.posts[0].subreddit.localeCompare(b.posts[0].subreddit)); // Sort by subreddit (alphabetical)
    } else if (filter === 'stock') {
      filtered = filtered.sort((a, b) => a.name.localeCompare(b.name)); // Sort by stock name (alphabetical)
    }
    
    setFilteredStocks(filtered);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>S&P 500 Stock Tracker</h1>
        <p>Tracking stocks mentioned on subreddits in the last hour</p>
      </header>

      <main className="stock-list">
        <div className="filter-section">
          <input 
            type="text" 
            placeholder="Search for stocks or subreddits..."
            onChange={(e) => setSearch(e.target.value)}
          />
          <label htmlFor="filter">Filter by: </label>
          <select id="filter" value={filter} onChange={(e) => setFilter(e.target.value)}>
            <option value="">Select Filter</option>
            <option value="mentions">Mentions (High to Low)</option>
            <option value="mentions-asc">Mentions (Low to High)</option>
            <option value="subreddit">Subreddit (Alphabetical)</option>
            <option value="stock">Stock Name (Alphabetical)</option>
          </select>
          <button onClick={applyFilter}>Apply Filter</button>
        </div>

        <div className="stock-cards">
          {filteredStocks.length > 0 ? (
            filteredStocks.map((stock, index) => (
              <div key={`${stock.symbol}-${index}`} className="stock-card">
                <h2>{stock.name} <span>({stock.symbol})</span></h2>
                <p>Mentions: <strong>{stock.mentions}</strong></p>
                <div className="posts-section">
                  {stock.posts.map((post, postIndex) => (
                    <div key={postIndex} className="post">
                      <h3>{post.title}</h3>
                      <p>{post.body}</p>
                      <p><strong>Subreddit:</strong> {post.subreddit}</p>
                      <p><strong>Author:</strong> {post.author}</p>
                      <small>{new Date(post.timestamp).toLocaleString()}</small>
                    </div>
                  ))}
                </div>
              </div>
            ))
          ) : (
            <p>No stocks mentioned in the last hour.</p>
          )}
        </div>

        {/* Add the BarChart component */}
        <div className="chart-section">
          <h2>Stock Mentions Bar Chart</h2>
          <BarChart data={filteredStocks} />
        </div>
      </main>
    </div>
  );
}

export default App;


