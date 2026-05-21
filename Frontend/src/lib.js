export const apibaseurl = "http://localhost:8000";
export const imgurl = import.meta.env.BASE_URL;
export function callApi(reqMethod, apiUrl, jsonData, formData, responseHandler, jwtToken = "")
{
    const headers = {};
    if (jsonData) headers["Content-Type"] = "application/json";
    if (jwtToken) headers["Token"] = jwtToken;

    const options = {
        method: reqMethod, 
        headers: headers, 
        body: jsonData ? JSON.stringify(jsonData) : formData ? formData : undefined
    };

    fetch(apiUrl, options)
        .then((res) => res.json())
        .then((data) => responseHandler(data))
        .catch((err) => alert(err));
}