#Shows all earnings for the day
def mostrar_resumen(ventas, total_recaudado):
    print("-----------------------------------")
    print("\nDAILY SALES SUMMARY: ")
    for producto, datos in ventas.items(): 
        print(f"Product: {producto}, Total quantity sold: {datos['cantidad']}")
        print("-----------------------------------")
    print(f"TOTAL COLLECTED FOR THE DAY: {total_recaudado}")

















<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Shattered Riffs</title>
    <link rel="shortcut icon" href="./assets/icons/logo.ico" type="image/x-icon">
    <link rel="stylesheet" href="./assets/css/style.css">
</head>
<body>

    <!-- HEADER -->
    <header class="header">
        <div class="container header__content">
            <img src="./assets/icons/logo.png" alt="">
            <h1 class="logo">Shattered Riffs</h1>



            <!-- Nav for desktop / hamburger for mobile -->
            <nav class="nav">
                <ul class="nav__list">
                    <li><a href="#events">Events</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#media">Media</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>

            <!-- Hint for JS (optional extra points) -->
            <button id="menu-toggle" onclick="ShowMenuphone()">
                ☰
            </button>
        </div>
    </header>

    <main>

        <!-- HERO -->
        <section class="hero">
            <div class="hero__overlay">
                 <ul>
            <li>
                <img src="./assets/img/img-2.jpg" alt="imagem-de-fondo">
            </li>
            <li>
                <img src="./assets/img/img-3.jpg" alt="img3">
            </li>
            <li>
                <img src="./assets/img/img-4.jpg" alt="img4">
            </li>
            <li>
                <img src="./assets/img/img-5.jpg" alt="img5">
            </li>
        </ul>
        <article class="texto-superpuesto">
                <h2>Rock the Night</h2>
                <p>Upcoming Tour</p>
                <a href="#events" class="btn">View Events</a>
        </article>
            </div>
        </section>

        <!-- EVENTS -->
        <section id="events" class="events container">
            <h2>Upcoming Events</h2>

            <!-- Extra points: table -->
            <table class="events__table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>City</th>
                        <th>Venue</th>
                        <th>Tickets</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>15 May</td>
                        <td>Madrid</td>
                        <td>Sala Sol</td>
                        <td><button>Buy</button></td>
                    </tr>
                    <tr>
                        <td>18 May</td>
                        <td>Barcelona</td>
                        <td>Razzmatazz</td>
                        <td><button>Buy</button></td>
                    </tr>
                    <tr>
                        <td>22 May</td>
                        <td>Valencia</td>
                        <td>Moon Club</td>
                        <td><button>Buy</button></td>
                    </tr>
                </tbody>
            </table>
        </section>

        <!-- ABOUT -->
        <section id="about" class="about container">
            <h2>About the Band</h2>

            <div class="about__content">
                <img src="./assets/img/img-1.jpg" alt="Band photo">

                <article>
                    <p>
                        Shattered Riffs is a high-energy rock band known for powerful live performances
                        and raw sound.
                    </p>

                    <!-- Required list -->
                    <h3>Our Influences</h3>
                    <ul>
                        <li>Classic Rock</li>
                        <li>Hard Rock</li>
                        <li>Alternative</li>
                    </ul>
                </article>
            </div>
        </section>

        <!-- MEDIA -->
        <section id="media" class="media container">
            <h2>Multimedia</h2>

            <div class="media__grid">
                <img src="./assets/img/img-2.jpg" alt="imagen2">
                <img src="./assets/img/img-3.jpg" alt="imagen3">
                <img src="./assets/img/img-4.jpg" alt="imagen4">
                <img src="./assets/img/img-5.jpg" alt="imagen5">
                <img src="./assets/img/img-6.jpg" alt="imagen6">
                <img src="./assets/img/img-7.jpg" alt="imagen7">
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer id="contact" class="footer">
        <div class="container footer__content">
            <p>© <span id="year"></span> Shattered Riffs</p>

            <!-- Another possible list -->
            <ul class="social">
                <li><a href="#">Instagram</a></li>
                <li><a href="#">Spotify</a></li>
                <li><a href="#">YouTube</a></li>
            </ul>
        </div>
    </footer>

    <script src="./assets/js/main.js"></script>
</body>
</html>












































* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #0b0b0f;
    color: #f5f5f5;
    line-height: 1.5;
}

.header {
    background: linear-gradient(rgba(0, 0, 0, 0.7)), rgba(0, 0, 0, 0.7)
}

.containerheader__content {
    background-size: cover;
    background-position: center;
    height: 300%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;

}

.nav__list {
    display: flex;
    list-style: none;
    gap: 20px;
    margin-top: 20px;
}

.nav__list a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.hero__overlay {
    width: 100%;
    height: 900px;
    overflow: hidden;
    position: relative;
}

.hero__overlay ul {
    display: flex;
    width: 400%;
    height: 400px;
    margin: 0;
    padding: 0;
    animation: cambio 20s infinite alternate ease;
}

.hero__overlay li {
    list-style: none;
    width: 25%;
    height: 100%;
}

.hero__overlay img {
    width: 100%;
    height: 900px;
    object-fit: cover;
    display: block;
}

.texto-superpuesto {
    color: #ffffff;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 20px;
    border-radius: 30px;
    transition: all 0.4s ease;
}

.Texto-superpuesto:hover {
    background-color: rgba(0, 0, 0, 0.5);

}

.Texto-superpuesto h2 {
    text-align: center;
}

.Texto-superpuesto p {
    text-align: center;
}

@keyframes cambio {
    0% {
        margin-left: 0%;
    }

    20% {
        margin-left: 0%;
    }

    25% {
        margin-left: -100%;
    }

    45% {
        margin-left: -100%;
    }

    50% {
        margin-left: -200%;
    }

    70% {
        margin-left: -200%;
    }

    75% {
        margin-left: -300%;
    }

    100% {
        margin-left: -300%;
    }
}

.btn {
    display: inline-block;
    padding: 0.8rem 2.5rem;
    background-color: rgba(190, 55, 55, 0.854);
    color: rgb(255, 255, 255);
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    border: none;
    cursor: pointer;
    transition: background-color 0.2s, color 0.2s;
    text-decoration: none;
}

img {
    max-width: 100%;
    display: block;
}

a {
    text-decoration: none;
    color: inherit;
}

main {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

section {
    margin: 3rem 0;
}

h1,
h2,
h3 {
    margin-bottom: 1rem;
}


/* Puedes usar esto si quieres centrar contenido */
/* .container {
    margin: 0 auto;
} */

button#menu-toggle {
    display: none;
}




@media (max-width: 768px) {
    button#menu-toggle {
        display: block;
    }

    nav.nav {
        display: none;
    }

    nav.nav.active {
        display: block !important
    }

    body {
        font-size: 14px;
    }

    main {
        width: 95%;
    }

    section {
        margin: 2rem 0;
    }

    /* Hint clave */
    /* piensa en:
       - menús colapsables
       - layouts en columna
       - imágenes adaptativas
    */
}














const date = new Date()
document.getElementById("year").innerText = date.getFullYear()

// Write your Js code here 

function showMenuphone() {
    var btn = document.getElementById("menu-toggle");
    var menu = document.getElementsByClassName("nav");
    if (menu[0].classList.contains("active")) {
        btn.innerText = "≡"
    } else {
        btn.innerText = "x"
    }
    menu[0].classList.toggle("active")
}





/* ===========================
   RESET & BASE
=========================== */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --color-bg: #0a0a0a;
    --color-surface: #111111;
    --color-accent: #e63946;
    --color-accent2: #ff6b35;
    --color-text: #f1f1f1;
    --color-muted: #888;
    --color-border: #2a2a2a;
    --font-display: 'Georgia', serif;
    --font-body: 'Trebuchet MS', sans-serif;
    --header-h: 70px;
}

html {
    scroll-behavior: smooth;
}

body {
    background-color: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-body);
    font-size: 16px;
    line-height: 1.6;
}

ul {
    list-style: none;
}

a {
    color: inherit;
    text-decoration: none;
}

img {
    display: block;
    max-width: 100%;
}

/* ===========================
   LAYOUT HELPERS
=========================== */
.container {
    width: 90%;
    max-width: 1100px;
    margin: 0 auto;
}

main {
    width: 100%;
}

section {
    margin: 4rem auto;
}

section h2 {
    font-family: var(--font-display);
    font-size: 2rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 1.5rem;
    color: var(--color-accent);
    border-bottom: 2px solid var(--color-accent);
    display: inline-block;
    padding-bottom: 4px;
}

/* ===========================
   HEADER
=========================== */
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: var(--header-h);
    background-color: rgba(0, 0, 0, 0.92);
    border-bottom: 1px solid var(--color-border);
    z-index: 100;
    backdrop-filter: blur(6px);
}

.header__content {
    display: flex;
    align-items: center;
    gap: 1rem;
    height: 100%;
}

.header__content img {
    width: 40px;
    height: 40px;
    object-fit: contain;
}

.logo {
    font-family: var(--font-display);
    font-size: 1.4rem;
    color: var(--color-accent);
    letter-spacing: 0.05em;
    white-space: nowrap;
    margin-right: auto;
}

/* NAV */
.nav__list {
    display: flex;
    gap: 1.5rem;
}

.nav__list a {
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--color-text);
    transition: color 0.2s;
}

.nav__list a:hover {
    color: var(--color-accent);
}

/* Hamburger button — hidden on desktop */
#menu-toggle {
    display: none;
    background: none;
    border: 1px solid var(--color-accent);
    color: var(--color-text);
    font-size: 1.3rem;
    padding: 4px 10px;
    cursor: pointer;
    border-radius: 4px;
}

/* ===========================
   HERO
=========================== */
.hero {
    margin-top: var(--header-h);
    position: relative;
    height: calc(100vh - var(--header-h));
    overflow: hidden;
}

.hero__overlay {
    position: relative;
    width: 100%;
    height: 100%;
}

/* Slideshow images */
.hero__overlay > ul {
    width: 100%;
    height: 100%;
    position: relative;
}

.hero__overlay > ul li {
    position: absolute;
    inset: 0;
    opacity: 0;
    animation: slideshow 16s infinite;
}

.hero__overlay > ul li:nth-child(1) { animation-delay: 0s; }
.hero__overlay > ul li:nth-child(2) { animation-delay: 4s; }
.hero__overlay > ul li:nth-child(3) { animation-delay: 8s; }
.hero__overlay > ul li:nth-child(4) { animation-delay: 12s; }

@keyframes slideshow {
    0%   { opacity: 0; }
    5%   { opacity: 1; }
    25%  { opacity: 1; }
    30%  { opacity: 0; }
    100% { opacity: 0; }
}

.hero__overlay > ul li img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.45);
}

/* Overlay text */
.texto-superpuesto {
    position: absolute;
    bottom: 15%;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    width: 90%;
    z-index: 2;
}

.texto-superpuesto h2 {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 8vw, 5rem);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--color-text);
    border: none;
    margin-bottom: 0.3rem;
    text-shadow: 0 0 30px rgba(230, 57, 70, 0.6);
}

.texto-superpuesto p {
    font-size: 1.1rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--color-accent2);
    margin-bottom: 1.5rem;
}

/* Button */
.btn {
    display: inline-block;
    padding: 0.7rem 2.2rem;
    background-color: var(--color-accent);
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 0.9rem;
    font-weight: bold;
    border-radius: 3px;
    transition: background 0.2s, transform 0.2s;
}

.btn:hover {
    background-color: var(--color-accent2);
    transform: translateY(-2px);
}

/* ===========================
   EVENTS
=========================== */
.events__table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
}

.events__table th,
.events__table td {
    padding: 0.8rem 1rem;
    text-align: left;
    border-bottom: 1px solid var(--color-border);
}

.events__table thead th {
    background-color: var(--color-surface);
    color: var(--color-accent);
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
}

.events__table tbody tr:hover {
    background-color: rgba(230, 57, 70, 0.07);
}

.events__table button {
    padding: 0.4rem 1.2rem;
    background-color: var(--color-accent);
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    transition: background 0.2s;
}

.events__table button:hover {
    background-color: var(--color-accent2);
}

/* ===========================
   ABOUT
=========================== */
.about__content {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
}

.about__content img {
    width: 45%;
    max-width: 400px;
    border-radius: 4px;
    object-fit: cover;
    filter: grayscale(20%);
}

.about__content article {
    flex: 1;
}

.about__content article p {
    margin-bottom: 1.2rem;
    color: #ccc;
    font-size: 1rem;
}

.about__content article h3 {
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--color-accent);
    margin-bottom: 0.6rem;
}

.about__content article ul {
    list-style: disc;
    padding-left: 1.3rem;
    color: #bbb;
}

.about__content article ul li {
    margin-bottom: 0.3rem;
}

/* ===========================
   MEDIA
=========================== */
.media__grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.8rem;
}

.media__grid img {
    width: 100%;
    aspect-ratio: 4/3;
    object-fit: cover;
    border-radius: 3px;
    filter: brightness(0.85);
    transition: filter 0.3s, transform 0.3s;
}

.media__grid img:hover {
    filter: brightness(1);
    transform: scale(1.03);
}

/* ===========================
   FOOTER
=========================== */
.footer {
    background-color: var(--color-surface);
    border-top: 1px solid var(--color-border);
    padding: 2rem 0;
    margin-top: 4rem;
}

.footer__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.footer__content p {
    color: var(--color-muted);
    font-size: 0.9rem;
}

.social {
    display: flex;
    gap: 1.5rem;
    list-style: none;
}

.social a {
    color: var(--color-muted);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    transition: color 0.2s;
}

.social a:hover {
    color: var(--color-accent);
}

/* ===========================
   MOBILE — MEDIA QUERIES
=========================== */
@media (max-width: 768px) {

    body {
        font-size: 14px;
    }

    main {
        width: 95%;
        margin: 0 auto;
    }

    section {
        margin: 2rem 0;
    }

    /* Header */
    .nav {
        display: none;
        position: absolute;
        top: var(--header-h);
        left: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.97);
        border-top: 1px solid var(--color-border);
        padding: 1rem 0;
    }

    .nav.open {
        display: block;
    }

    .nav__list {
        flex-direction: column;
        align-items: center;
        gap: 1.2rem;
    }

    #menu-toggle {
        display: block;
    }

    /* About: stack vertically */
    .about__content {
        flex-direction: column;
    }

    .about__content img {
        width: 100%;
        max-width: 100%;
    }

    /* Media grid: 2 columns */
    .media__grid {
        grid-template-columns: repeat(2, 1fr);
    }

    /* Events table: scroll horizontally */
    .events__table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
    }

    /* Footer */
    .footer__content {
        flex-direction: column;
        text-align: center;
    }
}






// ===========================
// Year in footer
// ===========================
document.getElementById('year').textContent = new Date().getFullYear();

// ===========================
// Hamburger menu (mobile)
// ===========================
function ShowMenuphone() {
    const nav = document.querySelector('.nav');
    nav.classList.toggle('open');
}

















