let btn = document.querySelector("#btnPrueba");
btn.addEventListener("click", (e) => {
    e.preventDefault();
    logJSONData();
})

async function logJSONData() {
    const response = await fetch("http://vps-3145377-x.dattaweb.com", {
        method: "GET", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        }
    });
    const jsonData = await response.json();
    console.log(jsonData);

}