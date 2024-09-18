import streamlit as st

#Variabler
enkelbiljett = 1
returbiljett = 2 * 0.8
VIPbiljett = 1.2
u18pris = 130
vuxenpris = 200
pensionpris = 100
saldo = 0
#-------------------------------------------------------------------------
st.title('Tågbolaget')
st.subheader('Ange ditt saldo')
upsaldo =st.number_input('Ange belopp här')
saldo = saldo + upsaldo
st.write(f'Uppdaterat saldo till {saldo}kr')
#--------------------------------------------------------------------------
st.header('Välj biljettyp nedanför')
biljettval = st.selectbox('Vilken biljettyp vill du ha?',('enkel', 'retur', 'VIP')
)
#--------------------------------------------------------------------------
st.header('Vänligen ange din ålder')
age =st.slider("Ange här", min_value=1, max_value=100, value=None, step=1)
#--------------------------------------------------------------------------
if age < 18 and biljettval == 'enkel':
    saldo=saldo - u18pris * enkelbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('Ha en trevlig resa!')
elif age < 18 and biljettval == 'retur':
    saldo=saldo - u18pris * returbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('Ha en trevlig resa!')
elif age < 18 and biljettval == 'VIP':
    saldo=saldo - u18pris * VIPbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettval == 'enkel':
    saldo=saldo - vuxenpris * enkelbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('ha en trevlig resa!')
elif 18 <= age <= 64 and biljettval == 'retur':
    saldo=saldo - vuxenpris * returbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('ha en trevlig resa!')
elif 18 <= age <= 64 and biljettval == 'VIP':
    saldo=saldo - vuxenpris * VIPbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('ha en trevlig resa!')
elif 64 < age <= 100 and biljettval == 'enkel':
    saldo=saldo - pensionpris * enkelbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 100 and biljettval == 'retur':
    saldo=saldo - pensionpris * returbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 100 and biljettval == 'VIP':
    saldo=saldo - pensionpris * VIPbiljett
    st.write(f'Tack för ditt köp! Ditt nya saldo är {saldo}kr.')
    st.subheader('Ha en trevlig resa!')
else:
    st.error('Ogiltligt svar försök igen!')
