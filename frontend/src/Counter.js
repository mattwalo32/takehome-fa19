import React, { Component } from 'react'


class Counter extends Component {
  
  constructor(props){
    super(props);
    this.state = {
      count: props.count
    };

    this.inc = this.inc.bind(this);
    this.dec = this.dec.bind(this);
  }
  
  componentWillReceiveProps(props) {
    if(props.inc){
      this.setState(state => ({
        count: state.count + 1
      }));
    }
  }

  inc() {
    this.setState(state => ({
      count: state.count + 1
    }))
  };
  
  dec() {
    this.setState(state => ({
      count: state.count - 1
    }))
  };

  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <div>
          <button type="button" onClick={this.inc}>inc</button>
          <button type="button" onClick={this.dec}>dec</button>
        </div>
      </div>
    )
  }
}

export default Counter
