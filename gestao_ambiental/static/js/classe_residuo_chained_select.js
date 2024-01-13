document.addEventListener('DOMContentLoaded', function () {
    var dropdown = document.getElementById('id_id_tp_residuos');
    var classeResiduo = document.getElementById('id_classe_residuo');

    function updateClasseResiduo() {
        var selectedValue = dropdown.value;
        classeResiduo.value = '';
        // Check if selectedValue is not empty
        if (selectedValue) {
            // Make an AJAX request to your server with the selected value
            fetch('/tipo_residuos/get_class/?id_tp_residuos=' + selectedValue)
                .then(response => response.json())
                .then(data => {
                    // Update the classe_residuo field with the returned data
                    classeResiduo.value = data.classe;
                });
        }
    }
    dropdown.addEventListener('change', updateClasseResiduo);
    updateClasseResiduo();
});
