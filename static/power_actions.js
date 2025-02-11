function power_button() {
  fetch('/power_button')
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}

function reset_hold() {
  fetch('/reset_hold')
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}

function reset_release() {
  fetch('/reset_release')
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}

function power_state() {
  fetch('/power_state')
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}