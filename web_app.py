import streamlit as st

# Título
st.title('ALC Bebidas')
opc = st.sidebar.selectbox('Selecione uma ação', ('Adicionar produto', 'Listar produto', 'Remover produto'))

# Inicializar Base de dados
if 'lista_produtos' not in st.session_state:
    st.session_state.lista_produtos = [
        # {'id': 1, 'Nome': 'Coca-cola lata 300ml', 'Preço': 4.75, 'Quantidade em estoque': 10},
        # {'id': 2, 'Nome': 'Skol lata 300ml', 'Preço': 6.75, 'Quantidade em estoque': 10},
        # {'id': 3, 'Nome': 'Guaraná lata 300ml', 'Preço': 3.75, 'Quantidade em estoque': 10},
        # {'id': 4, 'Nome': 'Itaipava lata 370ml', 'Preço': 5.75, 'Quantidade em estoque': 10},
    ]

# Listar produtos
def listar_produtos():
    if len(st.session_state.lista_produtos) == 0:
        st.write('Lista de produtos vazia !')
    else:
        st.subheader('Lista de produtos')
        for produtos in st.session_state.lista_produtos:
            st.write(f'|ID: {produtos['id']}\n|NOME: {produtos['Nome']}\n|PREÇO: R${produtos['Preço']}\n|QUANTIDADE EM ESTOQUE: {produtos['Quantidade em estoque']}')

# Adicionar produto
def adiciona_produto():
    st.subheader('Adicionar produto')
    nome_produto = st.text_input('Nome do produto')
    preco = st.number_input('Preço do produto')
    quantidade_estoque = st.number_input('Quantidade em estoque')
    if st.button('Adicionar'):
        novo_produto = {'id': len(st.session_state.lista_produtos) + 1, 'Nome': nome_produto, 'Preço': preco, 'Quantidade em estoque': quantidade_estoque}
        st.session_state.lista_produtos.append(novo_produto)
        st.success('Produto adicionado com sucesso !')

# Remove produto
def remover_produto():
    st.subheader('Remover produto')
    id_produto = st.number_input('Digite o ID do produto pra ser removido: ')
    if st.button('Remover produto'):
        produto_encontrado = False
        for prod in st.session_state.lista_produtos:
            if prod['id'] == id_produto:
                st.session_state.lista_produtos.remove(prod)
                produto_encontrado = True

    st.success(f'Produto com id {id_produto} removido com sucesso !')
        
        

# Barra lateral
if opc == 'Adicionar produto':
    adiciona_produto()
elif opc == 'Listar produto':
    listar_produtos()
elif opc == 'Remover produto':
    remover_produto()