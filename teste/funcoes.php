<?php
// Conexão com o banco de dados
$host = "localhost";
$user = "root";
$pass = "";
$dbname = "formulario_db";

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Função para listar todos os contatos
function listarContatos() {
    global $conn;
    $sql = "SELECT * FROM contatos";
    $result = $conn->query($sql);
    $contatos = [];
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $contatos[] = $row;
        }
    }
    return $contatos;
}

// Função para adicionar um contato
function adicionarContato($nome, $email) {
    global $conn;
    $sql = "INSERT INTO contatos (nome, email) VALUES ('$nome', '$email')";
    $conn->query($sql);
}

// Função para editar um contato
function editarContato($id) {
    global $conn;
    $sql = "SELECT * FROM contatos WHERE id=$id";
    $result = $conn->query($sql);
    return $result->fetch_assoc();
}

// Função para atualizar um contato
function atualizarContato($id, $nome, $email) {
    global $conn;
    $sql = "UPDATE contatos SET nome='$nome', email='$email' WHERE id=$id";
    $conn->query($sql);
}

// Função para excluir um contato
function excluirContato($id) {
    global $conn;
    $sql = "DELETE FROM contatos WHERE id=$id";
    $conn->query($sql);
}
?>
