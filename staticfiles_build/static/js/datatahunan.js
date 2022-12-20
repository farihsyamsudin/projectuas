// Olah Data Start

let totalEtem = 0
let totalJapuh = 0
let totalKuniran = 0
let totalLayang = 0
let totalSelar = 0
let totalTembang = 0
let totalTengkek = 0
let totalTeri = 0
let totalTongkol = 0
let totalBondolan = 0
let totalCumi = 0

let totalData = []

// Jumlah Data Tiap Tahun
// datahasil tangkap = dikirim dari model Hasiltangkap
  datahasiltangkap.forEach(e => {
    let tahun = e.fields.tanggal_datang.substr(0,4)

      totalEtem = totalEtem + e.fields.etem 
      totalJapuh = totalJapuh + e.fields.japuh 
      totalKuniran = totalKuniran + e.fields.kuniran
      totalLayang = totalLayang + e.fields.layang
      totalSelar = totalSelar + e.fields.selar
      totalTembang = totalTembang + e.fields.tembang 
      totalTengkek = totalTengkek + e.fields.tengkek 
      totalTeri = totalTeri + e.fields.teri
      totalTongkol = totalTongkol + e.fields.tongkol 
      totalBondolan = totalBondolan + e.fields.bondolan 
      totalCumi = totalCumi + e.fields.cumi

      totalDatas = totalEtem + totalJapuh + totalKuniran + totalLayang + totalSelar + totalTembang + totalTengkek + totalTeri + totalTongkol + totalBondolan + totalCumi
      
      totalData.push([tahun, totalDatas])

      totalEtem = 0
      totalJapuh = 0 
      totalKuniran = 0
      totalLayang = 0
      totalSelar = 0
      totalTembang = 0 
      totalTengkek = 0
      totalTeri = 0
      totalTongkol = 0
      totalBondolan = 0 
      totalCumi = 0
    });
    
// Olah Data End


// Jumlah Tangkapan Perhun Start

// Initialize an empty result array
let result = [];

// Use the reduce() method to sum the values for each year
totalData.reduce((acc, cur) => {
  // Check if the year already exists in the result array
  let yearIndex = result.findIndex(item => item[0] === cur[0]);
  if (yearIndex === -1) {
    // If the year does not exist in the result array, add it
    result.push([cur[0], cur[1]]);
  } else {
    // If the year exists in the result array, add the value to the existing sum
    result[yearIndex][1] += cur[1];
  }
}, 0);

// The result array should now contain the desired values

// Di sort biar kalo masukin tahun terdahulu, datanya ga ngacak
result.sort((a, b) => {
  return a[0] - b[0];
});

console.log(result)
// Jumlah Tangkapan Pertahun End

// Jumlah Trip Start
var jmltrip = totalData.reduce(function(acc, element) {
  var year = element[0];
  if (acc[year] === undefined) {
    acc[year] = 1;
  } else {
    acc[year]++;
  }
  return acc;
}, {});
console.log(jmltrip)
// Jumlah Trip End

// Analisis CPUE Start

var CPUE = {}

var CPUE = result.reduce(function(acc, element) {
  var year = element[0];
  var value = element[1];
  acc[year] = value / jmltrip[year];
  return acc;
}, {});


// Analisis CPUE End

// Diganti ke array biar bisa dimasukin grafik
CPUE = Object.entries(CPUE)
jmltrip = Object.entries(jmltrip)
// Diganti ke array biar bisa dimasukin grafik

const grafik = document.getElementById('GrafikPenangkapan').getContext('2d');

const labels = ['2020','2021', '2022', '2023', '2024', '2025']
const datagrafik = {
    labels: labels,
    datasets: [{
        label: 'Jumlah Tangkapan (Kg)',
        data: result,
        borderWidth: 1
      }, {
        label: 'CPUE (Catch Per Unit Effort) / Kg',
        data: CPUE,
        borderWidth: 1
      }, {
        label: 'Jumlah Trip / Effort',
        data: jmltrip,
        borderWidth: 1
      }]
};

new Chart(grafik, {
    type: 'line',
    data: datagrafik,
    options: {

    }
});