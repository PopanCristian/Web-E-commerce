let slideIndex = 1;

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");

  if (slides.length === 0) return;

  if (n > slides.length) {
    slideIndex = 1;
  }

  
  if (n < 1) {
    slideIndex = slides.length;
  }

  
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[slideIndex - 1].style.display = "block";
}

document.addEventListener("DOMContentLoaded", function() {
  if (document.getElementsByClassName("mySlides").length > 0) {
    showSlides(slideIndex);
  }
});

window.addEventListener('scroll', function() {
  let scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

  document.querySelector('.first-title').style.transform = `translateX(${scrollPosition * -1}px)`;

  document.querySelector('.second-title').style.transform = `translateX(${scrollPosition * 1}px)`;
});

//GoogleMapsAPI js code

async function initMap() {
  
  const position = { lat: 47.6491390989744, lng: 23.573060774989063 };
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  map = new Map(document.getElementById("map"), {
    zoom: 16,
    center: position,
    mapId: "664218f131cbb1d3",
    disableDefaultUI: true,

  });
  const pinSvgString = `
    <svg version="1.1" id="Layer_1" width="50" height="50" x="0px" y="0px" viewBox="0 0 512.001 512.001" style="enable-background:new 0 0 512.001 512.001;" xmlns="http://www.w3.org/2000/svg">
      <polygon style="fill:#FEC566;" points="403.683,85.254 381.078,7.495 130.925,7.495 108.318,85.254 256.001,113.915 "/>
      <polygon style="opacity:0.1;enable-background:new;" points="158.286,85.254 180.893,7.495 130.925,7.495 108.318,85.254   256.001,113.915 280.985,109.066 "/>
      <path style="fill:#FEA001;" d="M256.001,113.915l-143.53,28.661l39.29,341.516c1.338,11.633,11.187,20.414,22.896,20.414h162.686  c11.71,0,21.558-8.78,22.896-20.414l39.29-341.516L256.001,113.915z"/>
      <path style="opacity:0.1;enable-background:new;" d="M201.73,484.091l-39.29-341.516l118.546-23.672l-24.984-4.989  l-143.53,28.661l39.29,341.516c1.338,11.633,11.187,20.414,22.896,20.414h49.968C212.917,504.505,203.068,495.724,201.73,484.091z"/>
      <path style="fill:#B8703F;" d="M443.61,117.704c-3.948-18.905-20.613-32.45-39.927-32.45H108.318  c-19.313,0-35.978,13.545-39.927,32.45l-5.194,24.871h385.605L443.61,117.704z"/>
      <path style="opacity:0.1;enable-background:new;" d="M158.286,85.254h-49.968c-19.313,0-35.978,13.545-39.927,32.45  l-5.194,24.871h49.968l5.194-24.871C122.308,98.799,138.974,85.254,158.286,85.254z"/>
      <path style="fill:#B8703F;" d="M380.53,228.043H131.472c-11.303,0-20.083,9.848-18.791,21.078l14.997,130.365  c1.098,9.547,9.181,16.753,18.791,16.753h219.062c9.61,0,17.693-7.206,18.791-16.753l14.998-130.365  C400.613,237.891,391.833,228.043,380.53,228.043z"/>
      <text style="font-family: Arial, sans-serif; font-size: 80px; font-style: italic; font-weight: 700; letter-spacing: 4.3px; word-spacing: 4.9px; white-space: pre;" x="170.115" y="308.311">Terra</text>
    </svg>`;
    const parser = new DOMParser();
    const pinSvg = parser.parseFromString(pinSvgString, "image/svg+xml").documentElement;

  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    content: pinSvg,
    title: "Terra",
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.container');
  const loginButtonOverlay = document.getElementById('login');
  const registerButtonOverlay = document.getElementById('register');

  if ( registerButtonOverlay && loginButtonOverlay){
  registerButtonOverlay.addEventListener('click', () => {
      container.classList.add("right-panel-active");
  });

  loginButtonOverlay.addEventListener('click', () => {
      container.classList.remove("right-panel-active");
  });
}
});
  

function enableEdit() {
  let inputFields = ['email','phone','first_name','last_name']
  inputFields.forEach(  field =>{

    let input = document.getElementById(field);
    input.removeAttribute("readonly");
    input.style.backgroundColor = "#fff";
    
  });
 
  document.getElementById("save-btn").style.display = "block";
}

