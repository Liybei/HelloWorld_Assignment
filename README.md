let paleta_fundo = "#1d1d1b";
let paleta_cores = [
  "#ffb000",
  "#ff4200",
  "#7da030",
  "#ff99cc",
  "#1d1d1b",
  "#f2f2e7",
];

// Set initial time
let segundos = 0;  // Initial seconds
let minutos = 0;   // Initial minutes
let horas = 0;     // Initial hours

let min_blocos = []; // Array to store minute blocks
let hora_blocos = []; // Array to store hour blocks

function setup() {
  createCanvas(600, 600);  // Create a 600x600 canvas
}

function draw() {
  background(paleta_fundo); // Set the background color

  // Update the seconds
  segundos++;
  if (segundos >= 60) {
    segundos = 0;
    minutos++;
    
    // When 60 seconds have passed, add a minute block
    min_blocos.push({ 
      x: random(50, width - 50), 
      y: random(300, height - 100), 
      color: random(paleta_cores) 
    });

    if (minutos >= 60) {
      minutos = 0;
      
      // When 60 minutes have passed, add an hour block
      hora_blocos.push({ 
        x: random(50, width - 50), 
        y: random(50, 200), 
        color: random(paleta_cores) 
      });
    }
  }

  // Draw all minute blocks
  for (let m of min_blocos) {
    fill(m.color); // Set the fill color
    noStroke;      // No border
    rect(m.x, m.y, 40, 40); // 40x40 minute block
  }

  // Draw all hour blocks
  for (let h of hora_blocos) {
    fill(h.color); // Set the fill color
    noStroke();    // No border
    rect(h.x, h.y, 60, 60); // 60x60 hour block
  }

  // Display time information (hours:minutes:seconds)
  fill("#f2f2e7");
  textSize(16);
  textAlign(CENTER, CENTER);
  text(nf(horas, 2) + ":" + nf(minutos, 2) + ":" + nf(segundos, 2), width / 2, height - 30);
}
