const API_ENDPOINT = "https://localhost:8000"

export function search(formData) {
    console.log("hit")
    const query = formData.get("query");
    alert(`You searched for ${query}`);
    // add backend search logic here
    const response = await fetch(`${API_ENDPOINT}/`)
}