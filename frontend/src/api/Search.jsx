const API_ENDPOINT = "http://localhost:800"

export default function search_post(query) {
    try {
        const response = await fetch(`${API_ENDPOINT}`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(query)
        })

        if (!response.ok) {
            throw new Error("network error occured")
        }
        const data = await response.json();
        // for now show data
        console.log(data)
    }
}