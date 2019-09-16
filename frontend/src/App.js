import React, { Component } from 'react'
import Instructions from './Instructions'
import Contact from './Contact'
import Counter from './Counter'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      contacts: [
        {id: 1, name: "Angad", nickname: "greg", hobby: "dirty-ing"},
        {id: 2, name: "Roy", nickname: "uwu", hobby: "weeb"},
        {id: 3, name: "Daniel", nickname: "oppa", hobby: "losing money with options trading"},
      ],
      name: "",
      nickname: "",
      hobby: "",
      inc: false
    }

    this.createContact = this.createContact.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  createContact() {
    let contact = {
      id: this.state.contacts.length,
      name: this.state.name,
      nickname: this.state.nickname,
      hobby: this.state.hobby
    };

    let newContacts = this.state.contacts;
    newContacts.push(contact);

    this.setState({
      inc: true,
      contacts: newContacts
    });
  }

  handleInputChange(event) {
    const value = event.target.value;
    const name = event.target.name;

    this.setState({
      [name]: value,
      inc: false
    });
  }

  render() {
    return (
      <div className="App" >
        <Instructions complete="true" />
        
        {this.state.contacts.map(x => (
          <Contact id={x.id} name={x.name} nickname={x.nickname} hobby={x.hobby} />
        ))}
        
        <br />
        <Counter count={0} inc={this.state.inc}/>
        <br />

        <h2>Create new Contact</h2>
        <form>
          <p>Enter Name</p>
          <input name="name" value={this.state.name} onChange={this.handleInputChange}  type="text" />
          <p>Enter Nickname</p>
          <input name="nickname" value={this.state.nickname} onChange={this.handleInputChange} type="text" />
          <p>Enter Hobby</p>
          <input name="hobby" value={this.state.hobby} onChange={this.handleInputChange} type="text" />
          <br />
          <button type="button" onClick={this.createContact}>Submit</button>
        </form>
      </div>
    )
  }
}

export default App