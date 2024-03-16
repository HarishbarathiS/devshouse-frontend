// script to make the components draggle using interact.js

interact(".draggable").draggable({
  // enable inertial throwing
  inertia: true,
  // keep the element within the area of it's parent
  modifiers: [
    interact.modifiers.restrictRect({
      restriction: "parent",
      endOnly: true,
    }),
  ],
  // enable autoScroll
  autoScroll: true,

  listeners: {
    // call this function on every dragmove event
    move: dragMoveListener,
  },
});

function dragMoveListener(event) {
  var target = event.target;
  // keep the dragged position in the data-x/data-y attributes
  var x = (parseFloat(target.getAttribute("data-x")) || 0) + event.dx;
  var y = (parseFloat(target.getAttribute("data-y")) || 0) + event.dy;

  // translate the element
  target.style.transform = "translate(" + x + "px, " + y + "px)";

  // update the position attributes
  target.setAttribute("data-x", x);
  target.setAttribute("data-y", y);
}

// this function is used later in the resizing and gesture demos
window.dragMoveListener = dragMoveListener;

//script to zoom in and out

var scale = 0.5; // Initial scale level
const ZOOM_SPEED = 0.03;
const MAX_SCALE = 0.6;
document.addEventListener("wheel", (e) => {
  if (e.deltaY > 0) {
    scale -= ZOOM_SPEED;
  } else {
    scale += ZOOM_SPEED;
  }
  scale = Math.min(scale, MAX_SCALE); // Maximum scale limit
  document.body.style.transform = `scale(${scale})`;
});

let isPanning = false;
let startX = 0,
  startY = 0;
let offsetX = 0,
  offsetY = 0; // Track the cumulative offsets

document.addEventListener("mousedown", (e) => {
  isPanning = true;
  startX = e.clientX;
  startY = e.clientY;
});

document.addEventListener("mousemove", (e) => {
  if (isPanning) {
    offsetX += e.clientX - startX;
    offsetY += e.clientY - startY;
    startX = e.clientX;
    startY = e.clientY;
    document.body.style.transform = `translate(${offsetX}px, ${offsetY}px) scale(${scale})`;
  }
});

document.addEventListener("mouseup", () => {
  isPanning = false;
});
