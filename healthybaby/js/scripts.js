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

    document.addEventListener("DOMContentLoaded", function () {
        // Botões de consulta
        document.querySelectorAll(".consultaButton").forEach(button => {
            button.addEventListener("click", function () {
                let gestanteId = this.getAttribute("data-id");
                window.location.href = `/consultas/${gestanteId}/`;  // Redireciona para a página de consultas com ID
            });
        });

        // Botões de informações
        document.querySelectorAll(".infoButton").forEach(button => {
            button.addEventListener("click", function () {
                let nome = this.getAttribute("data-nome");
                let cpf = this.getAttribute("data-cpf");
                let telefone = this.getAttribute("data-telefone");
                let nascimento = this.getAttribute("data-nascimento");
                let parto = this.getAttribute("data-parto");

                alert(`Nome: ${nome}\nCPF: ${cpf}\nTelefone: ${telefone}\nNascimento: ${nascimento}\nParto: ${parto}`);
            });
        });
    });

});
