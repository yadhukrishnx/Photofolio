


// Function to apply the theme based on the given mode
function applyTheme(mode) {
  const root=document.documentElement;
  const themeIcon = document.getElementById('theme-icon');
  const mobilenav= document.getElementById('mobile-nav-toggle');
  if ( mode === 'dark' ) {
   
    root.style.setProperty('--background-color', '#ffffff'); 
    root.style.setProperty('--default-color', '#000000'); 
    root.style.setProperty('--heading-color', '#000000');
    root.style.setProperty('--accent-color', '#288c6c'); 
    root.style.setProperty('--contrast-color', '#000000');
    // Change icon to indicate light mode
    themeIcon.classList.remove('bi-brightness-alt-high-fill');
    themeIcon.classList.add('bi-moon-fill');
    mobilenav.classList.add('text-dark');
    
  } 
  else {

    root.style.setProperty('--background-color', '#000000'); 
    root.style.setProperty('--default-color', '#fafafa'); 
    root.style.setProperty('--heading-color', '#ffffff');
    root.style.setProperty('--accent-color', '#0bb680'); 
    root.style.setProperty('--contrast-color', '#161718');
    // Change icon to indicate dark mode
    themeIcon.classList.remove('bi-moon-fill');
    themeIcon.classList.add('bi-brightness-alt-high-fill');
    mobilenav.classList.remove('text-dark');
    
  }
}

// Function to toggle the theme


// Check the saved theme on page load
document.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('theme') || 'dark';

  applyTheme(savedTheme);


});

function themetoggle() {
  let currentTheme = localStorage.getItem('theme');

  if (currentTheme === 'dark') {
      localStorage.setItem('theme', 'light');
      applyTheme('light');
  } 
  else {
      localStorage.setItem('theme', 'dark');
      applyTheme('dark');
  }
}




(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      if (document.querySelector('.mobile-nav-active')) {
        e.preventDefault();
        this.parentNode.classList.toggle('active');
        this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
        e.stopImmediatePropagation();
      }
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      setTimeout(() => {
        preloader.classList.add('loaded');
      }, 500);
      setTimeout(() => {
        preloader.remove();
      }, 500);
    });
  }

  /**
   * Scroll top button    
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  const glightbox = glightbox({
    selector: '.glightbox'
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll('.swiper').forEach(function(swiper) {
      let config = JSON.parse(swiper.querySelector('.swiper-config').innerHTML.trim());
      new Swiper(swiper, config);
    });
  }
  window.addEventListener('load', initSwiper);

})();