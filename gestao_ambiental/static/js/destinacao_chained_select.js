document.addEventListener('DOMContentLoaded', function () {
    var fornecedorDropdown = document.getElementById('id_id_fornecedor_destinacao');
    var destinacaoDropdown = document.getElementById('id_id_destinacao');

    var selectedValue = fornecedorDropdown.value;
    if (selectedValue === "") {
        destinacaoDropdown.setAttribute('disabled', 'disabled');
        destinacaoDropdown.innerHTML = '';  // Clear the dropdown
    }

    fornecedorDropdown.addEventListener('change', function () {
        var selectedValue = this.value;

        if (selectedValue === "") {
            destinacaoDropdown.innerHTML = "";
            destinacaoDropdown.setAttribute('disabled', 'disabled');
        } else {
            destinacaoDropdown.removeAttribute('disabled');

            // Make an AJAX request to your server with the selected value
            fetch('/fornecedor/get_destinacao/?id=' + selectedValue)
                .then(response => response.json())
                .then(data => {
                    var jsonData = JSON.parse(data);
                    // Clear the existing options in destinacaoDropdown
                    destinacaoDropdown.innerHTML = '';
                    // Add the new options to destinacaoDropdown
                    jsonData.forEach(function (destinacao) {
                        var opt = document.createElement('option');
                        opt.value = destinacao.pk;
                        opt.textContent = destinacao.fields.nome;
                        destinacaoDropdown.appendChild(opt);
                    });
                });
        }
    });
});
