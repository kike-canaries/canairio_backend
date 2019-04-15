import React, {Component} from "react";
import ReactDOM from "react-dom";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import NotFound from "./components/NotFound";
import Sensors from "./components/Sensors";
import {Provider} from "react-redux";

import {createStore} from "redux";
import sensorsApp from "./reducers";

let store = createStore(sensorsApp);

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <BrowserRouter>
                    <Switch>
                        <Route exact path="/" component={Sensors}/>
                        <Route component={NotFound}/>
                    </Switch>
                </BrowserRouter>
            </Provider>
        );
    }
}

export default App;

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App/>, wrapper) : null;
