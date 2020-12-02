import './App.css';
import React, { useState } from 'react';

function App() {
  const [op, setOp] = useState(3);
  const [res, setRes] = useState('texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto ');

  return (
    <div className="container">
      <div className="opSelector">
        <div className={"opSelectorButton " + (op === 0 ? "selected " : "")} onClick={() => setOp(0)}>
          <p className="opSelectorButtonText">Get</p>
        </div>
        <div className={"opSelectorButton " + (op === 1 ? "selected " : "")} onClick={() => setOp(1)}>
          <p className="opSelectorButtonText">Set</p>
        </div>
        <div className={"opSelectorButton " + (op === 2 ? "selected " : "")} onClick={() => setOp(2)}>
          <p className="opSelectorButtonText">Del</p>
        </div>
        <div className={"opSelectorButton " + (op === 3 ? "selected " : "")} onClick={() => setOp(3)}>
          <p className="opSelectorButtonText">TestAndSet</p>
        </div>
      </div>
      <div className="inputOutputContainer">
        <div className="inputButtonDiv">
          <div className="inputDataContainer">
            {op === 0 ?
              <div className="inputAnsDiv">
                <div>Key:</div>
                <input />
              </div>
              : op === 1 ?
                <div className="inputGroup">
                  <div className="inputAnsDiv">
                    <div>Key:</div>
                    <input />
                  </div>
                  <div className="inputAnsDiv">
                    <div>TS:</div>
                    <input />
                  </div>
                  <div className="inputAnsDiv">
                    <div>Data:</div>
                    <input />
                  </div>
                </div>
                : op === 2 ?
                  <div className="inputGroup">
                    <div className="inputAnsDiv">
                      <div>Key:</div>
                      <input />
                    </div>
                    <div className="inputAnsDiv">
                      <div>Vers:</div>
                      <input placeholder="opcional" />
                    </div>

                  </div>
                  :
                  <div className="inputGroup">
                    <div className="inputAnsDiv">
                      <div>Key:</div>
                      <input />
                    </div>
                    <div className="inputAnsDiv">
                      <div>NewVers:</div>
                      <input />
                    </div>
                    <div className="inputAnsDiv">
                      <div>TS:</div>
                      <input />
                    </div>
                    <div className="inputAnsDiv">
                      <div>Data:</div>
                      <input />
                    </div>
                    <div className="inputAnsDiv">
                      <div>Vers:</div>
                      <input />
                    </div>
                  </div>
            }
          </div>
          <div className='sendButton'>
            Ir
        </div>
        </div>

        <div className="outputDataContainer">
            {res}
        </div>
      </div>
    </div>

  );
}

export default App;
