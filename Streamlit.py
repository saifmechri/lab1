import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Afficher un message simple
st.write('Hello World')

# Demander à l'utilisateur d'entrer un film préféré
x = st.text_input('Favorite Movie?')
st.write(f"Your favorite movie is: {x}")

# Afficher un bouton et exécuter une action lorsque l'utilisateur clique dessus
is_clicked = st.button("Click Me")

# Afficher un titre H2
st.write("## This is a H2 Title!")

# Utiliser markdown pour formater le texte
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# Lecture du fichier CSV (assure-toi que le fichier 'movies.csv' existe dans le répertoire)
try:
    data = pd.read_csv("movies.csv")
    st.write(data)  # Affiche les données du CSV sous forme de tableau
except FileNotFoundError:
    st.error("movies.csv not found in the current directory.")

# Données aléatoires pour les graphiques
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

# Afficher des graphiques
st.bar_chart(chart_data)
st.line_chart(chart_data)

# Calcul des paiements hypothécaires
st.title("Mortgage Repayments Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)  # Créer deux colonnes
# Entrée de données pour la valeur de la maison, le dépôt, le taux d'intérêt, etc.
home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

# Calcul du montant du prêt et des paiements mensuels
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Afficher les résultats des paiements
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)  # Créer trois colonnes pour afficher les résultats
col1.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

# Créer un tableau avec l'échéancier des paiements
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)  # Calculer l'année du prêt
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Afficher le plan de paiement sous forme de graphique
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)
