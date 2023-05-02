import Splide from '@splidejs/splide';
import tippy from 'tippy.js';



document.addEventListener( 'DOMContentLoaded', function() {
    new Splide( '.splide__container.vertical .splide',
                {
                    type: 'loop',
                    direction: 'ttb',
                    perPage: 3,
                    perMove: 1,
                    height: '12rem',
                    arrows: false,
                    pagination: false,
                    paginationKeyboard: false,
                    drag: false,
                    autoplay: true,
                    pauseOnOver: false,
                    pauseOnFocus: false,
                    interval: 2000,
                }).mount();
    let perPage = 3;
    let height = "4rem";
    new Splide( '.splide__container.horizontal .splide',
                {
                    type: 'loop',
                    direction: 'rtl',
                    perPage: 2,
                    perMove: 1,
                    height: '4rem',
                    arrows: false,
                    pagination: false,
                    paginationKeyboard: false,
                    drag: false,
                    autoplay: true,
                    pauseOnOver: false,
                    pauseOnFocus: false,
                    interval: 2000,
                }).mount();
    tippy('[data-tippy-content]');
} );
