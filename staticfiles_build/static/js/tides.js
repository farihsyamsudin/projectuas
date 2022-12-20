// Cari Tanggal buat Fetch Start

let month = new Date().getMonth()
    month += 1 
    month.toString() 
    let dummyMonth = '0'    
    
    let day = new Date().getDate().toString()
    let dummyDay = '0'    

    let year = new Date().getFullYear()

    // Month Handler 
    if (month.length === 1) {
        dummyMonth += month
    } else {
        dummyMonth = month
    }

    // Day Handler
    if (day.length === 1) {
        dummyDay += day
    } else {
        dummyDay = day
    }
        
const dateNow = [year, dummyMonth, dummyDay]
const date = dateNow.join('-')

// Cari Tanggal buat fetch End

const map = L.map('map',{
    scrollWheelZoom : false,
}).setView([-5.995555, 106.171065], 11);
const responseTides = document.getElementById('responseTides');
const loader = document.getElementById('loader');

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 12,
    minZoom: 9,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const myIcon = L.icon({
    iconUrl: '/static/img/port.png',
    iconSize: [45, 45],
    // iconAnchor: [22, 94],
    // popupAnchor: [-3, -76],
    // shadowUrl: 'my-icon-shadow.png',
    // shadowSize: [68, 95],
    // shadowAnchor: [22, 94]
});

const PPN = L.marker([-6.030577870474317, 106.16413686808463], {icon: myIcon}).addTo(map).bindPopup('PPN Karangantu')
.openPopup();

const getData = async (lat, lon) =>{
    const options = {
        url: `https://www.worldtides.info/api/v3?extremes&date=${date}&lat=${lat}&lon=${lon}&key=${key}`,
        method: 'GET',
    };

    await axios(options)
    .then(response => {
        // console.log(response.data);
        if (response.status === 200) {
            // Apoch to locale string Start
            response.data.extremes.forEach(e => {
                e.dt = new Date(e.dt*1000).toLocaleString()
            });
            // Apoch to locale string End

            // Handler Station Start
            if (!response.data.station) {
                response.data.station = "null"
            }
            // Handler Station End

            // Response if Ok
            responseTides.innerHTML = `
            <div class="text-center px-6 md:text-xl text-lg">
            <h3 class="pb-4">Atlas : ${response.data.atlas}</h3>
            <h3 class="pb-4">Nearby Station : ${response.data.station}</h3>
            <h3>Request Wilayah : </h3> 
            <h6 class="pb-4">Lat : ${response.data.requestLat} Lon : ${response.data.requestLon}</h6>
            <h3>Response Wilayah : </h3> 
            <h6 class="pb-4">Lat : ${response.data.responseLat} Lon : ${response.data.responseLon}</h6>
            </div>
            <div class="w-full overflow-x-auto px-6">
                <table class="w-[90%] mx-auto">
                <thead>
                    <tr class="[&>*]:py-2 [&>*]:px-6 bg-blue-700 text-white">
                        <th>Waktu gelombang pasang</th>
                        <th>Tinggi gelombang pasang (m)</th>
                        <th>Tipe</th>
                    </tr>
                </thead>
                <tbody>
                    ` + response.data.extremes.map(e =>{
                        return(`
                            <tr class="[&>*]:py-2 [&>*]:px-6 odd:bg-blue-400 even:bg-blue-500">
                                <td>${e.dt}</td>
                                <td>${e.height}</td>
                                <td>${e.type}</td>
                            </tr>
                        `)
                    }) +`
                </tbody>
                </table>
            </div>
            <div class="text-center px-6 py-10">
            <h3>CopyRight : </h3> 
            <h6>${response.data.copyright}</h6>
            </div>
            `
            loader.classList.toggle('scale-0')
            // Response if Ok
        }
    })
    .catch((err) => {
        // console.log(err.response.data)
        if (err.response.data.status === 400 && err.response.data.error === 'Not enough credits') {
            responseTides.innerHTML = `
            <div class='text-center px-10'>
                <h3 class='text-xl text-center'>
                    Kredit Tidak Cukup.
                    Error ini dikarenakan API key pada website, Mohon
                    <a href="mailto:farihsyamsudin31@upi.edu?subject=API%20KEY&body=API%20KEY%20on%20your%20ocenao.com%20website%20is%20not%20enough%20credits%2C%20please%20check%20it%20later!"> Klik disini!</a> atau 
                    <a target='_blank' rel='noreferrer' href="https://mail.google.com/mail/?view=cm&fs=1&to=farihsyamsudin31@upi.edu&su=API%20KEY&body=API%20KEY%20on%20your%20website%20is%20not%20enough%20credits%2C%20please%20check%20it%20later!"> Disini</a> untuk kontak admin   
                </h3>
                <h3 class='pt-4 text-center'>atau masukkan API key mu sendiri <input id="APIKeyInput" class='border mx-1 my-2 px-4 py-1 rounded-lg border-teal-600 focus:outline-none' type="text" /> <button onclick="setAPIKeyHandler()" class='py-2 px-4 bg-teal-600 rounded-lg text-white'>Enter!</button></h3>
                <a href="https://www.worldtides.info/register" target='_blank' rel='noreferrer'><h4 class=''>Dapatkan API Key mu disini!</h4></a>
            </div>
            
            `
            loader.classList.toggle('scale-0')
        } else if (err.response.data.status === 400 && err.response.data.error === 'API key is invalid'){
            responseTides.innerHTML = `
                <h2 class="px-6 py-2 text-center text-xl">API KEY INVALID! Refresh Website!</h2>            
            `
            loader.classList.toggle('scale-0')
        }
    });;
}

map.on('click', function(e) {
    if (confirm(`Anda akan melihat informasi gelombang di lat : ${e.latlng.lat} lon: ${e.latlng.lng}`)) {
        loader.classList.toggle('scale-0')
        let lat = e.latlng.lat
        let lon = e.latlng.lng
    
        // if (map.hasLayer(marker)) {
        //     map.removeLayer(marker);
        // }
        
        let marker = L.marker([lat, lon]).addTo(map);
    
        getData(lat, lon)
    }

});

const setAPIKeyHandler = (e) =>{
    key = document.getElementById('APIKeyInput').value
    // getData()

    responseTides.innerHTML = `
    <h1 class="px-6 py-2 text-center text-xl">Klik kembali lokasi pada peta!</h1>             
    `
}