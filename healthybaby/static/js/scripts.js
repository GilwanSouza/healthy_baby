/*!
* Start Bootstrap - Agency v7.0.4 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    navbarShrink();

    document.addEventListener('scroll', navbarShrink);

    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    document.getElementById("togglePassword").addEventListener("click", function () {
        let passwordField = document.getElementById("password");
        let icon = this.querySelector("i");

        if (passwordField.type === "password") {
            passwordField.type = "text";
            icon.classList.remove("bi-eye");
            icon.classList.add("bi-eye-slash");
        } else {
            passwordField.type = "password";
            icon.classList.remove("bi-eye-slash");
            icon.classList.add("bi-eye");
        }
    });

    document.getElementById("id_cpf").addEventListener("input", function(event) {
        let cpf = event.target.value;
        cpf = cpf.replace(/\D/g, "");
        cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
        cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
        cpf = cpf.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
        event.target.value = cpf;
    });

    document.getElementById("togglePassword").addEventListener("click", function () {
        let passwordField = document.getElementById("password");
        let icon = this.querySelector("i");

        if (passwordField.type === "password") {
            passwordField.type = "text";
            icon.classList.remove("bi-eye");
            icon.classList.add("bi-eye-slash");
        } else {
            passwordField.type = "password";
            icon.classList.remove("bi-eye-slash");
            icon.classList.add("bi-eye");
        }
    });

    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".consultaButton").forEach(button => {
            button.addEventListener("click", function () {
                let gestanteId = this.getAttribute("data-id");
                window.location.href = `/consultas/${gestanteId}/`;
            });
        });

        document.querySelectorAll(".infoButton").forEach(button => {
            button.addEventListener("click", function () {
                let nome = this.getAttribute("data-nome");
                let cpf = this.getAttribute("data-cpf");
                let telefone = this.getAttribute("data-telefone");
                let nascimento = this.getAttribute("data-nascimento");
                let parto = this.getAttribute("data-parto");
                let url = this.getAttribute("data-url");
                    window.location.href = url;

                alert(`Nome: ${nome}\nCPF: ${cpf}\nTelefone: ${telefone}\nNascimento: ${nascimento}\nParto: ${parto}`);
            });
        });
    });

    document.addEventListener("DOMContentLoaded", function() {
        const seatNumbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28,48,47,46,45,44,43,42,41,31,32,33,34,35,36,37,38];
        const seatsContainer = document.getElementById("seatsContainer");

        // Criar os botões dos assentos
        seatNumbers.forEach(num => {
            let seat = document.createElement("div");
            seat.classList.add("seat");
            seat.textContent = num;
            seat.setAttribute("data-number", num);

            // Adicionar evento de clique
            seat.addEventListener("click", function() {
                this.classList.toggle("selected");
            });

            seatsContainer.appendChild(seat);
        });

        // Botão de confirmação
        document.getElementById("confirmSelection").addEventListener("click", function() {
            let selectedSeats = [];
            document.querySelectorAll(".seat.selected").forEach(seat => {
                selectedSeats.push(seat.getAttribute("data-number"));
            });

            if (selectedSeats.length > 0) {
                alert("Assentos selecionados: " + selectedSeats.join(", "));
            } else {
                alert("Nenhum assento selecionado.");
            }
        });
    });

    document.addEventListener("DOMContentLoaded", function () {
        const urlParams = new URLSearchParams(window.location.search);

        document.getElementById("gestante_id").value = urlParams.get("id");
        document.getElementById("nome").value = urlParams.get("nome");
        document.getElementById("cpf").value = urlParams.get("cpf");
        document.getElementById("telefone").value = urlParams.get("telefone");
        document.getElementById("nascimento").value = urlParams.get("nascimento");
        document.getElementById("parto").value = urlParams.get("parto");
    });
});
