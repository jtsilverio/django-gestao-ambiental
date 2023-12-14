document.getElementById('id_estado').addEventListener('change', function () {
    // Get the selected state
    var selectedState = this.value;

    // Clear the cities dropdown
    var citySelect = document.getElementById('id_id_cidade');


    if (selectedState === "") {
        citySelect.innerHTML = "";
        citySelect.setAttribute('disabled', 'disabled');
    } else {
        // Fetch the cities for the selected state
        citySelect.removeAttribute('disabled');
        fetch('/cidades/get_cidades/?estado=' + selectedState)
            .then(response => response.json())
            .then(data => {
                var jsonData = JSON.parse(data);
                // Clear the existing options in unidadeDropdown
                citySelect.innerHTML = '';

                // Add each city to the cities dropdown
                jsonData.forEach(cidade => {
                    var option = document.createElement('option');
                    option.value = cidade.pk;
                    option.text = cidade.fields.nome;
                    citySelect.add(option);
                });
            });
    }
});
