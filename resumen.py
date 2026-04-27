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
























