export const apibaseurl = "http://localhost:8000";
export const imgurl = import.meta.env.BASE_URL;

export async function callApi(reqMethod, apiUrl, jsonData, formData, responseHandler, jwtToken = "")
{
    const headers = {};
    if (jsonData) headers["Content-Type"] = "application/json";
    if (jwtToken) headers["Token"] = jwtToken;

    const options = {
        method: reqMethod,
        headers: headers,
        body: jsonData ? JSON.stringify(jsonData) : formData ? formData : undefined
    };

    try {
        const res = await fetch(apiUrl, options);
        if (!res.ok) {
            let bodyText = "";
            try { bodyText = await res.text(); } catch(e) {}
            console.error("HTTP error", res.status, res.statusText, bodyText, reqMethod, apiUrl, options);
            alert(`HTTP ${res.status}: ${res.statusText}`);
            return;
        }

        let data;
        try {
            data = await res.json();
        } catch (e) {
            console.error("Failed to parse JSON response", e, reqMethod, apiUrl);
            alert("Invalid JSON response from server");
            return;
        }

        responseHandler(data);
    }
    catch (err) {
        console.error("Network/fetch error", err, reqMethod, apiUrl, options);
        alert(`Network error: ${err.message}\nRequest: ${reqMethod} ${apiUrl}`);
    }
}