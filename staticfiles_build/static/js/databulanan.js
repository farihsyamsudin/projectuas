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

// Jumlah Data Tiap Ikan
datahasiltangkap.forEach(e => {
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
});

// Olah Data End

const grafik = document.getElementById('GrafikPenangkapan')

const labels = ['Etem', 'Japuh', 'Kuniran', 'Layang', 'Selar', 'Tembang', 'Tengkek', 'Teri', 'Tongkol', 'Bondolan', 'Cumi']
const datagrafik = {
    labels: labels,
    datasets: [{
        label: 'Jumlah Tangkapan (Kg)',
        data: [totalEtem, totalJapuh, totalKuniran, totalLayang, totalSelar, totalTembang, totalTengkek, totalTeri, totalTongkol, totalBondolan, totalCumi],
        borderWidth: 1
      }]
};

var chart = new Chart(grafik, {
    type: 'bar',
    data: datagrafik,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
});
