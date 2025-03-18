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

        // Preenchendo os campos do modelo Gestante
        document.getElementById("gestante_id").value = urlParams.get("id");
        document.getElementById("nome").value = urlParams.get("nome");
        document.getElementById("cpf").value = urlParams.get("cpf");
        document.getElementById("telefone").value = urlParams.get("telefone");
        document.getElementById("nascimento").value = urlParams.get("nascimento");
        document.getElementById("parto").value = urlParams.get("parto");
        document.getElementById("endereco").value = urlParams.get("endereco");
        document.getElementById("ponto_referencia").value = urlParams.get("ponto_referencia");
        document.getElementById("estado").value = urlParams.get("estado");
        document.getElementById("cidade").value = urlParams.get("cidade");
        document.getElementById("cep").value = urlParams.get("cep");
        document.getElementById("num_sus").value = urlParams.get("num_sus");
        document.getElementById("num_nis").value = urlParams.get("num_nis");
        document.getElementById("nome_social").value = urlParams.get("nome_social");
        document.getElementById("nome_companheiro").value = urlParams.get("nome_companheiro");
        document.getElementById("email").value = urlParams.get("email");
        document.getElementById("ocupacao").value = urlParams.get("ocupacao");
        document.getElementById("etnia").value = urlParams.get("etnia");
        document.getElementById("raca").value = urlParams.get("raca");

        document.getElementById("emg_ctt_nome").value = urlParams.get("emg_ctt_nome");
        document.getElementById("emg_ctt_telefone").value = urlParams.get("emg_ctt_telefone");
        document.getElementById("emg_ctt_parentesco").value = urlParams.get("emg_ctt_parentesco");

        // Dados do parceiro
        document.getElementById("parceiro_nome").value = urlParams.get("parceiro_nome");
        document.getElementById("parceiro_nome_social").value = urlParams.get("parceiro_nome_social");
        document.getElementById("parceiro_instrucao").value = urlParams.get("parceiro_instrucao");
        document.getElementById("parceiro_idade").value = urlParams.get("parceiro_idade");
        document.getElementById("parceiro_peso").value = urlParams.get("parceiro_peso");
        document.getElementById("parceiro_altura").value = urlParams.get("parceiro_altura");
        document.getElementById("parceiro_imc").value = urlParams.get("parceiro_imc");
        document.getElementById("parceiro_perssaoarterial").value = urlParams.get("parceiro_perssaoarterial");
        document.getElementById("parceiro_antecedentes").value = urlParams.get("parceiro_antecedentes");
        document.getElementById("parceiro_info").value = urlParams.get("parceiro_info");

        // Exames laboratoriais
        document.getElementById("pcr_exame_abo_data").value = urlParams.get("pcr_exame_abo_data");
        document.getElementById("pcr_exame_abo_resultado").value = urlParams.get("pcr_exame_abo_resultado");
        document.getElementById("pcr_exame_glicemia_data").value = urlParams.get("pcr_exame_glicemia_data");
        document.getElementById("pcr_exame_glicemia_resultado").value = urlParams.get("pcr_exame_glicemia_resultado");
        document.getElementById("pcr_exame_hemograma_data").value = urlParams.get("pcr_exame_hemograma_data");
        document.getElementById("pcr_exame_hemograma_resultado").value = urlParams.get("pcr_exame_hemograma_resultado");
        document.getElementById("pcr_exame_hiv_data").value = urlParams.get("pcr_exame_hiv_data");
        document.getElementById("pcr_exame_hiv_resultado").value = urlParams.get("pcr_exame_hiv_resultado");
        document.getElementById("pcr_exame_sifilis_data").value = urlParams.get("pcr_exame_sifilis_data");
        document.getElementById("pcr_exame_sifilis_resultado").value = urlParams.get("pcr_exame_sifilis_resultado");
        document.getElementById("pcr_exame_vdrl_data").value = urlParams.get("pcr_exame_vdrl_data");
        document.getElementById("pcr_exame_vdrl_resultado").value = urlParams.get("pcr_exame_vdrl_resultado");
        document.getElementById("pcr_exame_hepatite_data").value = urlParams.get("pcr_exame_hepatite_data");
        document.getElementById("pcr_exame_hepatite_resultado").value = urlParams.get("pcr_exame_hepatite_resultado");

        // Preenchendo os campos do modelo PosParto
        document.getElementById("cpf_mae").value = urlParams.get("cpf_mae");
        document.getElementById("tipo_parto").value = urlParams.get("tipo_parto");
        document.getElementById("sangramento").value = urlParams.get("sangramento");
        document.getElementById("medicamentos").value = urlParams.get("medicamentos");
        document.getElementById("intercorrencias").value = urlParams.get("intercorrencias");
        document.getElementById("alta_maternidade").value = urlParams.get("alta_maternidade");
        document.getElementById("peso_alta").value = urlParams.get("peso_alta");
        document.getElementById("visita_domiciliar").value = urlParams.get("visita_domiciliar");
        document.getElementById("nascimento").value = urlParams.get("nascimento");

        document.getElementById("nome_bebe").value = urlParams.get("nome_bebe");
        document.getElementById("data_nascimento_bebe").value = urlParams.get("data_nascimento_bebe");
        document.getElementById("hora_nascimento_bebe").value = urlParams.get("hora_nascimento_bebe");
        document.getElementById("local_nascimento").value = urlParams.get("local_nascimento");
        document.getElementById("profissionais").value = urlParams.get("profissionais");

        // Preenchendo os campos do modelo Odonto
        document.getElementById("cpf_gestante").value = urlParams.get("cpf_gestante");
        document.getElementById("placa_viavel").value = urlParams.get("placa_viavel");
        document.getElementById("placa_viavel_data").value = urlParams.get("placa_viavel_data");
        document.getElementById("placa_sangramento").value = urlParams.get("placa_sangramento");
        document.getElementById("placa_sangramento_data").value = urlParams.get("placa_sangramento_data");
        document.getElementById("placa_sangramento_sondagem").value = urlParams.get("placa_sangramento_sondagem");
        document.getElementById("placa_sangramento_sondagem_data").value = urlParams.get("placa_sangramento_sondagem_data");
        document.getElementById("calculo_dentario").value = urlParams.get("calculo_dentario");
        document.getElementById("calculo_dentario_data").value = urlParams.get("calculo_dentario_data");
        document.getElementById("mobilidade").value = urlParams.get("mobilidade");
        document.getElementById("mobilidade_data").value = urlParams.get("mobilidade_data");
        document.getElementById("perda_insercao").value = urlParams.get("perda_insercao");
        document.getElementById("perda_insercao_data").value = urlParams.get("perda_insercao_data");
        document.getElementById("plano_tratamento").value = urlParams.get("plano_tratamento");
        document.getElementById("tratamento_data").value = urlParams.get("tratamento_data");
        document.getElementById("tratamento_dente").value = urlParams.get("tratamento_dente");
        document.getElementById("procedimento_realizado").value = urlParams.get("procedimento_realizado");
        document.getElementById("especialidade").value = urlParams.get("especialidade");
        document.getElementById("tratamento_necessario").value = urlParams.get("tratamento_necessario");
        document.getElementById("encaminhamento").value = urlParams.get("encaminhamento");
        document.getElementById("retorno").value = urlParams.get("retorno");
        document.getElementById("plano_cuidado").value = urlParams.get("plano_cuidado");

        // Preenchendo os campos do modelo Consulta
        document.getElementById("gestante").value = urlParams.get("gestante");
        document.getElementById("data_consulta").value = urlParams.get("data_consulta");
        document.getElementById("observacoes").value = urlParams.get("observacoes");
        document.getElementById("idade_gestacional").value = urlParams.get("idade_gestacional");
        document.getElementById("unidade_saude").value = urlParams.get("unidade_saude");
        document.getElementById("especialidade_consulta").value = urlParams.get("especialidade_consulta");
        document.getElementById("nome_profissional").value = urlParams.get("nome_profissional");
        document.getElementById("crm").value = urlParams.get("crm");
    });
    
    function filtrarConsulta() {
        var consultaSelect = document.getElementById('consulta_select');
        if (consultaSelect.value) {
            var modal = new bootstrap.Modal(document.getElementById('portfolioModalConsulta'));
            modal.show();
        }
    }
    
    function filtrarConsultaOdonto() {
        var odontoSelect = document.getElementById('odonto_select');
        if (odontoSelect.value) {
            var modal = new bootstrap.Modal(document.getElementById('portfolioModalOdonto'));
            modal.show();
        }
    }
    
    
});
