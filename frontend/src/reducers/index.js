import { combineReducers } from "redux";
import sensors from "./sensors";

const sensorsApp = combineReducers({
  sensors,
})

export default sensorsApp;
