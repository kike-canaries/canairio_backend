const initialState = [
    {
        id: null,
        mac: null,
        lat: null,
        lon: null,
        name: null
    }
];


export default function sensors(state = initialState, action) {
    switch (action.type) {
        default:
            return state;
    }
}
