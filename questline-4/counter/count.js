let number = 0;

function increase() {
  number = number + 1;
  document.getElementById("count").innerHTML = number;
}

function decrease() {
  number = number - 1;
  document.getElementById("count").innerHTML = number;
}
