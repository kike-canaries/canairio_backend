import React, {Component} from "react";
import DataProvider from "./DataProvider";
import Table from "./Table";

class Sensors extends Component {
    render() {
        return (
            <DataProvider endpoint="points/sensors/"
                render={data => <Table data={data} />} />
        );
    }
}

export default Sensors
