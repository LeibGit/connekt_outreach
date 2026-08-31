const API_ENDPOINT = "https://connekt-outreach.onrender.com"

export async function search(formData) {
    try {
        const query = formData.get("query");
        const qty = formData.get("number");
        alert(`You searched for ${query}, ${qty} candidates will be targeted.`);
        // add backend search logic here
        const response = await fetch(`${API_ENDPOINT}/search/candidates`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                query, 
                qty
            })
        })

        if (!response.ok) {
            throw new Error("network error occured")
        }
        const data = await response.json();
        return {
            "success": data.success, 
            "data": data.data, 
            "message": data.message
        }
    } catch(err) {
        console.log(err)
    }
}