// Get the container element
const container = document.getElementById("checkboxContainer");

// Define the number of checkboxes you want to create
const numberOfCheckboxes = 52;

// Array of labels for the checkboxes
const checkboxLabels = ['acidity', 'palpitations', 'anxiety', 'bladder_discomfort',
'blurred_and_distorted_vision', 'breathlessness', 'burning_micturition',
'chest_pain', 'chills', 'congestion', 'continuous_feel_of_urine',
'continuous_sneezing', 'cough', 'depression', 'dischromic _patches',
'drying_and_tingling_lips', 'excessive_hunger', 'fast_heart_rate',
'fatigue', 'foul_smell_of urine', 'headache', 'high_fever',
'indigestion', 'irritability', 'itching', 'lethargy',
'loss_of_appetite', 'loss_of_smell', 'malaise', 'mild_fever',
'muscle_pain', 'nausea', 'nodal_skin_eruptions', 'palpitations',
'phlegm', 'red_spots_over_body', 'redness_of_eyes', 'runny_nose',
'rusty_sputum', 'shivering', 'sinus_pressure', 'skin_rash',
'slurred_speech', 'spotting_ urination', 'stiff_neck', 'stomach_pain',
'sweating', 'swelled_lymph_nodes', 'throat_irritation',
'visual_disturbances', 'vomiting', 'watering_from_eyes'];

// Loop to create checkboxes
for (let i = 0; i < numberOfCheckboxes; i++) {
    // Create a new checkbox element
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.id = "checkbox" + i;
    checkbox.name = "checkbox" + i;

    // Create a label for the checkbox
    const label = document.createElement("label");
    label.htmlFor = "checkbox" + i;
    label.appendChild(document.createTextNode(checkboxLabels[i]));

    // Append the checkbox and label to the container
    container.appendChild(checkbox);
    container.appendChild(label);
    container.appendChild(document.createElement("br")); // Add a line break after each checkbox
}