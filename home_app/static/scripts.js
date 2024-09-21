let slideIndex = 1;
showSlides(slideIndex);

// Funcția pentru butoanele Next/Previous
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Funcția pentru punctele (dots)
function currentSlide(n) {
  showSlides(slideIndex = n);
}

// Funcția principală care afișează slide-urile
function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides"); // Selectează toate slide-urile

  // Revine la primul slide dacă n depășește numărul total de slide-uri
  if (n > slides.length) {
    slideIndex = 1;
  }

  // Revine la ultimul slide dacă n este mai mic decât 1
  if (n < 1) {
    slideIndex = slides.length;
  }

  // Ascunde toate slide-urile
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }


  // Afișează slide-ul curent și activează punctul corespunzător
  slides[slideIndex - 1].style.display = "block";
}

document.addEventListener("DOMContentLoaded", function() {
  showSlides(slideIndex); // Asigură-te că primul slide este afișat imediat ce pagina se încarcă
});

window.addEventListener('scroll', function() {
  let scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

  document.querySelector('.first-title').style.transform = `translateX(${scrollPosition * -1}px)`;

  document.querySelector('.second-title').style.transform = `translateX(${scrollPosition * 1}px)`;
});


