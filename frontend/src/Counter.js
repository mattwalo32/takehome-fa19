import React, { Component } from 'react'


class Counter extends Component {
  state = {
    count: 0
  }
  
  inc = () => {
    this.setState(({ count }) => ({
      count: count + 1
    }))
  };
  
  dec = () => {
    this.setState(({count}) => ({
      count: count - 1
    }))
  };


  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <div>
          <button onClick={this.inc}>inc</button>
          <button onClick={this.dec}>dec</button>
        </div>
      </div>
    )
  }
}

export default Counter
