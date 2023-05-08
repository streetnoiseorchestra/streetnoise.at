import Splide from '@splidejs/splide';
import tippy from 'tippy.js';



document.addEventListener( 'DOMContentLoaded', function() {
    if (document.querySelector(".splide")) {
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
        let height = "3rem";
        if (window.screen.width < 300) {
            perPage = 2;
            height = "4rem";
        } else if (window.screen.width < 400) {
            perPage = 2;
            height = "4rem";
        } else if (window.screen.width > 400) {
            perPage = 3;
            height = "3rem";
        }
        new Splide( '.splide__container.horizontal .splide',
                    {
                        type: 'loop',
                        direction: 'ltr',
                        fixedHeight: '3.7rem',
                        perPage: perPage,
                        perMove: 1,
                        height: height,
                        arrows: false,
                        pagination: false,
                        paginationKeyboard: false,
                        drag: false,
                        autoplay: true,
                        pauseOnOver: false,
                        pauseOnFocus: false,
                        interval: 2000,
                    }).mount();
    }
    tippy('[data-tippy-content]');
} );
