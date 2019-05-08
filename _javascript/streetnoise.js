import BulmaAccordion from 'bulma-accordion';

document.addEventListener('DOMContentLoaded', () => {
  var accordions = BulmaAccordion.attach();

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target  = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });

    var slider = tns({
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
  }
  console.log('LOADED');
});
