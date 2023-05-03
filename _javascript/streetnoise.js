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

///// START MODERNIZER with webp support
/*! modernizr 3.6.0 (Custom Build) | MIT *
 * https://modernizr.com/download/?-webp-setclasses !*/
!function(e,n,A){function o(e){var n=u.className,A=Modernizr._config.classPrefix||"";if(c&&(n=n.baseVal),Modernizr._config.enableJSClass){var o=new RegExp("(^|\\s)"+A+"no-js(\\s|$)");n=n.replace(o,"$1"+A+"js$2")}Modernizr._config.enableClasses&&(n+=" "+A+e.join(" "+A),c?u.className.baseVal=n:u.className=n)}function t(e,n){return typeof e===n}function a(){var e,n,A,o,a,i,l;for(var f in r)if(r.hasOwnProperty(f)){if(e=[],n=r[f],n.name&&(e.push(n.name.toLowerCase()),n.options&&n.options.aliases&&n.options.aliases.length))for(A=0;A<n.options.aliases.length;A++)e.push(n.options.aliases[A].toLowerCase());for(o=t(n.fn,"function")?n.fn():n.fn,a=0;a<e.length;a++)i=e[a],l=i.split("."),1===l.length?Modernizr[l[0]]=o:(!Modernizr[l[0]]||Modernizr[l[0]]instanceof Boolean||(Modernizr[l[0]]=new Boolean(Modernizr[l[0]])),Modernizr[l[0]][l[1]]=o),s.push((o?"":"no-")+l.join("-"))}}function i(e,n){if("object"==typeof e)for(var A in e)f(e,A)&&i(A,e[A]);else{e=e.toLowerCase();var t=e.split("."),a=Modernizr[t[0]];if(2==t.length&&(a=a[t[1]]),"undefined"!=typeof a)return Modernizr;n="function"==typeof n?n():n,1==t.length?Modernizr[t[0]]=n:(!Modernizr[t[0]]||Modernizr[t[0]]instanceof Boolean||(Modernizr[t[0]]=new Boolean(Modernizr[t[0]])),Modernizr[t[0]][t[1]]=n),o([(n&&0!=n?"":"no-")+t.join("-")]),Modernizr._trigger(e,n)}return Modernizr}var s=[],r=[],l={_version:"3.6.0",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,n){var A=this;setTimeout(function(){n(A[e])},0)},addTest:function(e,n,A){r.push({name:e,fn:n,options:A})},addAsyncTest:function(e){r.push({name:null,fn:e})}},Modernizr=function(){};Modernizr.prototype=l,Modernizr=new Modernizr;var f,u=n.documentElement,c="svg"===u.nodeName.toLowerCase();!function(){var e={}.hasOwnProperty;f=t(e,"undefined")||t(e.call,"undefined")?function(e,n){return n in e&&t(e.constructor.prototype[n],"undefined")}:function(n,A){return e.call(n,A)}}(),l._l={},l.on=function(e,n){this._l[e]||(this._l[e]=[]),this._l[e].push(n),Modernizr.hasOwnProperty(e)&&setTimeout(function(){Modernizr._trigger(e,Modernizr[e])},0)},l._trigger=function(e,n){if(this._l[e]){var A=this._l[e];setTimeout(function(){var e,o;for(e=0;e<A.length;e++)(o=A[e])(n)},0),delete this._l[e]}},Modernizr._q.push(function(){l.addTest=i}),Modernizr.addAsyncTest(function(){function e(e,n,A){function o(n){var o=n&&"load"===n.type?1==t.width:!1,a="webp"===e;i(e,a&&o?new Boolean(o):o),A&&A(n)}var t=new Image;t.onerror=o,t.onload=o,t.src=n}var n=[{uri:"data:image/webp;base64,UklGRiQAAABXRUJQVlA4IBgAAAAwAQCdASoBAAEAAwA0JaQAA3AA/vuUAAA=",name:"webp"},{uri:"data:image/webp;base64,UklGRkoAAABXRUJQVlA4WAoAAAAQAAAAAAAAAAAAQUxQSAwAAAABBxAR/Q9ERP8DAABWUDggGAAAADABAJ0BKgEAAQADADQlpAADcAD++/1QAA==",name:"webp.alpha"},{uri:"data:image/webp;base64,UklGRlIAAABXRUJQVlA4WAoAAAASAAAAAAAAAAAAQU5JTQYAAAD/////AABBTk1GJgAAAAAAAAAAAAAAAAAAAGQAAABWUDhMDQAAAC8AAAAQBxAREYiI/gcA",name:"webp.animation"},{uri:"data:image/webp;base64,UklGRh4AAABXRUJQVlA4TBEAAAAvAAAAAAfQ//73v/+BiOh/AAA=",name:"webp.lossless"}],A=n.shift();e(A.name,A.uri,function(A){if(A&&"load"===A.type)for(var o=0;o<n.length;o++)e(n[o].name,n[o].uri)})}),a(),o(s),delete l.addTest,delete l.addAsyncTest;for(var p=0;p<Modernizr._q.length;p++)Modernizr._q[p]();e.Modernizr=Modernizr}(window,document);
/// END MONDERIZER with webp
