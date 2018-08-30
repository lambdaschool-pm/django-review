import React, { Component } from 'react';
import axios from 'axios';
import { Wrapper } from './AppCss.js';

class App extends Component {
	componentDidMount() {
		axios.get('https://swipeanddine.herokuapp.com/api/foods/').then((results) => {
			console.log(results);
		});
	}
	render() {
		return <Wrapper>Hello World</Wrapper>;
	}
}

export default App;
