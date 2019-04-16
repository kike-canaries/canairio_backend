const initialState = [];


export default function sensors(state = initialState, action) {
    let sensorList = state.slice();
    switch (action.type) {
        case "ADD_SENSOR":
            return [...state, {mac: action.mac, lat: action.lat, lon: action.lon, name: action.name}];

        case "UPDATE_SENSOR":
            let sensorToUpdate = sensorList[action.id]
            sensorToUpdate.mac = action.mac;
            sensorToUpdate.lat = action.lat;
            sensorToUpdate.lon = action.lon;
            sensorToUpdate.name = action.name;
            sensorList.splice(action.id, 1, sensorToUpdate);
            return sensorList;

        case "DELETE_SENSOR":
            sensorList.splice(action.id, 1);
            return sensorList;
        default:
            return state;
    }
}
