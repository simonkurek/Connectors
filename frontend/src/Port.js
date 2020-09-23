import React from 'react';
import './Port.css'

export default class Port extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        items: []
      };
    }
  
    componentDidMount() {
      fetch("http://localhost:5000/")
        .then(res => res.json())
        .then(
          (result) => {
            console.log(result)
            this.setState({
              isLoaded: true,
              items: result
            });
          },
          // Uwaga: to ważne, żeby obsłużyć błędy tutaj, a
          // nie w bloku catch(), aby nie przetwarzać błędów
          // mających swoje źródło w komponencie.
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }

    render() {
      const { error, isLoaded, items } = this.state;
      if (error) {
        return <div>Błąd: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Ładowanie...</div>;
      } else {
        return (
          <ul>
            {items.map(item => (
                <div className="port-div">
                    <h2>{item.name}</h2>
                    <text>{item.desc}</text>
                    <img src={item.link}></img>
                </div>
            ))}
          </ul>
        );
      }
    }
  }