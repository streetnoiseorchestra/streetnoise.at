//import BulmaAccordion from 'bulma-accordion';
document.addEventListener('DOMContentLoaded', function () {
  if (typeof BulmaAccordion !== 'undefined') var accordions = BulmaAccordion.attach(); // Get all "navbar-burger" elements

  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0); // Check if there are any navbar burgers

  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(function (el) {
      el.addEventListener('click', function () {
        // Get the target from the "data-target" attribute
        var target = el.dataset.target;
        var $target = document.getElementById(target); // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"

        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
    if (document.getElementsByClassName('slider-wir').length > 0) tns({
      autoHeight: false,
      container: '.slider-wir',
      items: 1,
      slideBy: 'page',
      autoplay: true,
      controls: false,
      axis: 'vertical',
      mouseDrag: true,
      autoplayButtonOutput: false,
      // autoplayHoverPause: true,
      // swipeAngle: false,
      speed: 400
    });
    if (document.getElementsByClassName('carousel').length > 0) tns({
      container: '.carousel',
      nav: false,
      controlsContainer: ".carousel-controls",
      hasControls: true,
      autoWidth: true,
      items: 3,
      slideBy: 'page',
      autoplay: false,
      controls: true,
      mouseDrag: true,
      swipeAngle: false,
      autoplayButtonOutput: false,
      // autoplayHoverPause: true,
      // swipeAngle: false,
      speed: 600
    });
  }

  console.log('LOADED');
});