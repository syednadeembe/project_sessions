// Configure the base URL for the backend services
const baseUrl = "http://localhost:30080"; // Use the actual service name and port


// Function to update and display website hits
function updateHits() {
    const hitsElement = document.getElementById("hits");

    fetch(`${baseUrl}/hits`)
        .then(response => response.json())
        .then(data => {
            hitsElement.textContent = `Website Hits: ${data.hits}`;
        })
        .catch(error => {
            console.error("Error fetching hits:", error);
        });
}

// Function to calculate and display the result
function calculate(operation) {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const apiUrl = `${baseUrl}/${operation}?num1=${num1}&num2=${num2}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const resultElement = document.getElementById("result");
            resultElement.textContent = `Result: ${data.result}`;
            resultElement.style.display = "block"; // Display the result element
        })
        .catch(error => {
            console.error("Error:", error);
        });
}

// Attach event listeners to the operation buttons
document.getElementById("addBtn").addEventListener("click", () => calculate("add"));
document.getElementById("subtractBtn").addEventListener("click", () => calculate("subtract"));
document.getElementById("multiplyBtn").addEventListener("click", () => calculate("multiply"));
document.getElementById("divideBtn").addEventListener("click", () => calculate("divide"));

// Initial update and display of website hits
updateHits();