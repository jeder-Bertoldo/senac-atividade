
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciamento de Contatos</title>
</head>
<body>
    <h2>Formulário de Contato</h2>
    <form action="processa.php" method="POST">
        <input type="hidden" name="id" id="id">
        <label for="nome">Nome:</label><br>
        <input type="text" id="nome" name="nome" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <button type="submit" name="action" value="create">Adicionar</button>
        <button type="submit" name="action" value="update">Atualizar</button>
    </form>
    <h2>Lista de Contatos</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Ações</th>
        </tr>
        <?php
include 'funcoes.php';
$contatos = listarContatos();
foreach ($contatos as $contato) {
    echo "<tr>";
    echo "<td>" . $contato['id'] . "</td>";
    echo "<td>" . $contato['nome'] . "</td>";
    echo "<td>" . $contato['email'] . "</td>";
    echo "<td>
            <form style='display:inline;' action='processa.php' method='POST'>
                <input type='hidden' name='id' value='" . $contato['id'] . "'>
                <button type='submit' name='action' value='edit'>Editar</button>
            </form>
            <form style='display:inline;' action='processa.php' method='POST'>
                <input type='hidden' name='id' value='" . $contato['id'] . "'>
                <button type='submit' name='action' value='delete'>Excluir</button>
            </form>
          </td>";
    echo "</tr>";
}
?>

    </table>
</body>
</html>
