window.onload = function () {
    var tpCadastro = document.getElementById('id_tp_cadastro');
    var carga = document.getElementById('id_carga');
    var capacidade = document.getElementById('id_capacidade');
    var recuperacao = document.getElementById('id_recuperacao');

    // Disable the fields on page load
    carga.disabled = true;
    capacidade.disabled = true;
    recuperacao.disabled = true;

    function handleTpUnidadeChange() {
        var selectedOption = tpCadastro.options[tpCadastro.selectedIndex].value;
        if (selectedOption === '') {
            carga.disabled = true;
            capacidade.disabled = true;
            recuperacao.disabled = true;
        } else if (selectedOption === 'N' || selectedOption === 'R') {
            carga.disabled = false;
            capacidade.disabled = true;
            recuperacao.disabled = true;
        } else if (selectedOption === 'D') {
            carga.disabled = true;
            capacidade.disabled = false;
            recuperacao.disabled = false;
        }
    }

    tpCadastro.addEventListener('change', handleTpUnidadeChange);
    // Call the function at startup to set the initial state
    handleTpUnidadeChange();
}
