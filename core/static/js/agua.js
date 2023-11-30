document.addEventListener('DOMContentLoaded', function() {
    var clusterDropdown = document.getElementById('id_id_cluster');
    var unidadeDropdown = document.getElementById('id_id_unidade_consumo');

    var selectedValue = clusterDropdown.value;
    if (selectedValue === "") {
        unidadeDropdown.setAttribute('disabled', 'disabled');
        unidadeDropdown.innerHTML = '';  // Clear the dropdown
    }

    clusterDropdown.addEventListener('change', function() {
        var selectedValue = this.value;

        if (selectedValue === "") {
            unidadeDropdown.innerHTML = "";
            unidadeDropdown.setAttribute('disabled', 'disabled');
        } else {
            unidadeDropdown.removeAttribute('disabled');

            // Make an AJAX request to your server with the selected value
            fetch('/unidade_consumo/get_unidades_consumo/?id_cluster=' + selectedValue)
                .then(response => response.json())
                .then(data => {
                    var jsonData = JSON.parse(data);
                    // Clear the existing options in unidadeDropdown
                    unidadeDropdown.innerHTML = '';
                    // Add the new options to unidadeDropdown
                    jsonData.forEach(function(unidade) {
                        var opt = document.createElement('option');
                        opt.value = unidade.pk;
                        opt.textContent = unidade.fields.nome;
                        unidadeDropdown.appendChild(opt);
                    });
                });
        }
    });
});
