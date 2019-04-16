import React, {Component} from "react";
import {connect} from "react-redux";

import {sensors} from "../actions";

class Sensor extends Component {

    state = {
        mac: "",
        lat: "",
        lon: "",
        name: "",
        updateSensorId: null,
    }

    resetForm = () => {
        this.setState({mac: "", lat: "", lon: "", name: "", updateSensorId: null});
    }

    selectForEdit = (id) => {
        let sensor = this.props.sensors[id];
        this.setState({mac: sensor.mac, lat: sensor.lat, lon: sensor.lon, name: sensor.name, updateSensorId: id});
    }

    submitSensor = (e) => {
        e.preventDefault();
        if (this.state.updateSensorId === null) {
            this.props.addSensor(this.state.mac, this.state.lat, this.state.lon, this.state.name);
        } else {
            this.props.updateSensor(this.state.updateSensorId, this.state.mac, this.state.lat, this.state.lon, this.state.name);
        }
        this.resetForm();
    }

    render() {
        return (
            <div>
                <h2>Welcome to Canairio!</h2>
                <hr/>

                <h3>Sensors</h3>
                <table>
                    <tbody>
                    {this.props.sensors.map(sensor => (
                        <tr key={`sensor_${sensor.mac}`}>
                            <td>{sensor.mac}</td>
                            <td>{sensor.lat}</td>
                            <td>{sensor.lon}</td>
                            <td>{sensor.name}</td>
                            <td>
                                <button>edit</button>
                            </td>
                            <td>
                                <button onClick={() => this.props.deleteSensor(id)}>delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
                <h3>Add new note</h3>
                <form onSubmit={this.submitSensor}>
                    <input
                        value={this.state.mac}
                        placeholder="Enter mac here..."
                        onChange={(e) => this.setState({mac: e.target.value})}
                        required/>
                    <input
                        value={this.state.lat}
                        placeholder="Enter lat here..."
                        onChange={(e) => this.setState({lat: e.target.value})}
                        required/>
                    <input
                        value={this.state.lon}
                        placeholder="Enter lon here..."
                        onChange={(e) => this.setState({lon: e.target.value})}
                        required/>
                    <input
                        value={this.state.name}
                        placeholder="Enter name here..."
                        onChange={(e) => this.setState({name: e.target.value})}
                        required/>
                    <button onClick={this.resetForm}>Reset</button>
                    <input type="submit" value="Save Sensor"/>
                </form>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        sensors: state.sensors,
    }
}

const mapDispatchToProps = dispatch => {
    return {
        addSensor: (mac, lat, lon, name) => {
            dispatch(sensors.addSensor(mac, lat, lon, name));
        },
        updateSensor: (id, mac, lat, lon, name) => {
            dispatch(sensors.addSensor(id, mac, lat, lon, name));
        },
        deleteSensor: (id) => {
            dispatch(sensors.deleteSensor(id));
        },
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Sensor);
