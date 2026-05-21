import streamlit as st
st.title("FastWay - Aluguel de Carros")
st.sidebar.title("Escolha o seu modelo")
st.sidebar.image("logo2.png")

carros = ['BMW', 'Civic', 'McLaren', 'Fusca-Azul', 'Subaru', 'Kawasaki-Ninja']

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado? ')
km = st.text_input(f'Quantos km você rodou com o {opcao}? ')

if opcao == 'BMW':
    diaria = 1500
elif opcao == 'Civic':
    diaria = 850
elif opcao == 'McLaren':
    diaria = 50000
elif opcao == 'Fusca-Azul':
    diaria = 450
elif opcao == 'Subaru':
    diaria = 1700
elif opcao == 'Kawasaki-Ninja':
    diaria = 10000


if st.button('Calcular'):
    dias = int(dias)
    km = float(km)
    
    total_dias = dias*diaria
    total_km = km*0.15
    aluguel_total = total_dias+total_km

    st.warning(f"Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f} ")