const targetDate = new Date("June 19, 2025 00:00:00").getTime();
const countdownEl = document.getElementById("countdown");

function updateCountdown() {

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hrs = Math.floor((diff / (1000*60*60)) % 24);
  const mins = Math.floor((diff / (1000*60)) % 60);
  const secs = Math.floor((diff / 1000) % 60);
  countdownEl.innerHTML = `${days} Hari ${hrs} Jam ${mins} Menit ${secs} Detik`;
}
setInterval(updateCountdown, 1000);
updateCountdown();