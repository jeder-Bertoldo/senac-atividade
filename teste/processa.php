<?php
include 'funcoes.php';

// Verificar a ação do formulário
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = isset($_POST['id']) ? $_POST['id'] : '';
    $nome = isset($_POST['nome']) ? $_POST['nome'] : '';
    $email = isset($_POST['email']) ? $_POST['email'] : '';
    $action = $_POST['action'];

    if ($action === 'create') {
        adicionarContato($nome, $email);
    } elseif ($action === 'update') {
        atualizarContato($id, $nome, $email);
    } elseif ($action === 'delete') {
        excluirContato($id);
    } elseif ($action === 'edit') {
        $contato = editarContato($id);
        echo "<script>
                document.getElementById('id').value = '".$contato['id']."';
                document.getElementById('nome').value = '".$contato['nome']."';
                document.getElementById('email').value = '".$contato['email']."';
              </script>";
    }
    header('Location: index.php');
    exit;
}
?>
