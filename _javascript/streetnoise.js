import BulmaAccordion from 'bulma-accordion';
import MediaElement from 'mediaelement';

function showConfirmation() {
  Array.from(document.getElementsByClassName("form-view")).forEach(el => el.classList.add("is-hidden"))
  Array.from(document.getElementsByClassName("success-view")).forEach(el => el.classList.remove("is-hidden"))
}
function getFieldForInput(field_id) {
  return document.getElementById(field_id).closest(".field")
}
function enableErrors(field) {
  let e = field.querySelector('.control')
  if(e)
    e.classList.add("has-icons-right")
  e = field.querySelector('input')
  if(e)
    e.classList.add("is-danger")
  e = field.querySelector('.error-icon')
  if(e)
    e.classList.remove("is-hidden")
  e = field.querySelector('.error-message')
  if(e)
    e.classList.remove("is-hidden")
}

function disableErrors(field) {
  let e = field.querySelector('.control')
  if(e)
    e.classList.remove("has-icons-right")
  e = field.querySelector('input')
  if(e)
    e.classList.remove("is-danger")
  e = field.querySelector('.error-icon')
  if(e)
    e.classList.add("is-hidden")
  e = field.querySelector('.error-message')
  if(e)
    e.classList.add("is-hidden")
  e = field.querySelector('.error-message')
  if(e)
    e.textContent = ""
}
function displayError(field_id, msgs) {
  const field = document.getElementById(field_id)
  if(!field) return;
  msgs.forEach(msg => {

    const fieldElement = getFieldForInput(field_id)
    enableErrors(fieldElement)
    fieldElement.querySelector('.error-message').textContent = msg
  })
}
async function newsletterSubscribeErrors(response) {
  const payload = await response.json()
  if(!payload.errors) {
    console.log("TODO display generic error message")
    return
  }
  console.log(payload.errors)
  Object.keys(payload.errors).forEach(field_id => {
    displayError(field_id, payload.errors[field_id])
  })
}

function disableAllErrors(form) {
  Array.from(form.querySelector('.field').children).forEach(disableErrors)
}

function setupNewsletterSubscribe() {
  const form = document.getElementById("newsletter_subscribe_form")
  if (!form) {
    return;
  }
  form.onsubmit = async(e) => {
    e.preventDefault();
    disableAllErrors(form)
    const data = new FormData(e.target)
    const response = await postNewsletterSubscribe(form.action, data)
    if ( response.status == 400) {
      return newsletterSubscribeErrors(response)
    }
    showConfirmation()
  }

}
async function postNewsletterSubscribe(url, data) {
  return fetch(url, {
    method: 'POST',
    body: data
  })
}

document.addEventListener('DOMContentLoaded', () => {
  setupNewsletterSubscribe();

  BulmaAccordion.attach();

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

    if(document.getElementsByClassName('slider-wir').length > 0)
      tns({
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
    if(document.getElementsByClassName('carousel').length > 0)
      tns({
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
        speed: 600
      });

    if(document.querySelector('audio')) {
      const player = new MediaElementPlayer(document.querySelector('audio'), {
        //pluginPath: "/path/to/shims/",
        // When using `MediaElementPlayer`, an `instance` argument
        // is available in the `success` callback
        success: function(mediaElement, originalNode, instance) {
          // do things
        }
      });
    }
  }
});
