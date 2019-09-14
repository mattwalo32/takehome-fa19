import React, { Component } from 'react'

class App extends Component {
  // YOUR CODE GOES BELOW



  render() {
    return (
      <div>
        <h2>{this.props.name}</h2>
        <ul>
          <li>
            {this.props.id}
          </li>

          <li>
            {this.props.nickname}
          </li>

          <li>
            {this.props.hobby}
          </li>
        </ul>
      </div>
    )
  }
}

export default App
