export const addSensor = (mac, lat, lon, name) => {
  return {
    type: "ADD_SENSOR",
    mac, lat, lon, name
  }
}

export const updateSensor = (id, mac, lat, lon, name) => {
  return {
    type: "UPDATE_SENSOR",
    id,
    mac, lat, lon, name
  }
}

export const deleteSensor = id => {
  return {
    type: "DELETE_SENSOR",
    id
  }
}
