import React from 'react';

const HistoryPanel = ({ history, show }) => (
  <div className={`history-panel${show ? ' show' : ''}`} aria-label="history">
    <div className="history-title">History</div>
    <div className="history-title-line"></div>
    <div className="history-list">
      {history.length === 0 ? (
        <div className="history-empty">No calculations yet.</div>
      ) : (
        history.map((item, idx) => (
          <div key={idx} className="history-item">
            <span className="history-expression">{item.expression}</span>
            <span className="history-equals"> = </span>
            <span className="history-result">{item.result}</span>
          </div>
        ))
      )}
    </div>
  </div>
);

export default HistoryPanel;
