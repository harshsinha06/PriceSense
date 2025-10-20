window.onload = function() {
    loadLocations();
};

function loadLocations() {
    axios.get("http://127.0.0.1:5000/get_location_names")
        .then(function(response) {
            const locations = response.data.locations;
            const uiLocations = document.getElementById("uiLocations");
            uiLocations.innerHTML = "";
            locations.forEach(function(loc) {
                let opt = document.createElement("option");
                opt.value = loc;
                opt.text = loc;
                uiLocations.appendChild(opt);
            });
        })
        .catch(function(error) {
            console.error("Error loading locations:", error);
        });
}

document.getElementById("priceForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const sqft = parseFloat(document.getElementById("uiSqft").value);
    const bhk = parseInt(document.getElementById("uiBHK").value);
    const bath = parseInt(document.getElementById("uiBath").value);
    const location = document.getElementById("uiLocations").value;

    // Send as form data, not params
    const formData = new URLSearchParams();
    formData.append("total_sqft", sqft);
    formData.append("bhk", bhk);
    formData.append("bath", bath);
    formData.append("location", location);

    axios.post("http://127.0.0.1:5000/predict_home_price", formData)
    .then(function(response) {
        document.getElementById("uiEstimatedPrice").innerHTML =
            `<h2>Estimated Price: ₹ ${response.data.estimated_price} Lakh</h2>`;
    })
    .catch(function(error) {
        document.getElementById("uiEstimatedPrice").innerHTML =
            `<h2 style="color:red;">Error estimating price</h2>`;
        console.error("Prediction error:", error);
    });
});