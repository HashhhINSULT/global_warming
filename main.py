
from flask import Flask, render_template, request

app = Flask(__name__)

emission_factors = {
    'transport_bus': 0.8,
    'transport_metro': 0.5,
    'transport_car': 5,
    'transport_motorcycle': 2,
    'transport_train': 0.6,
    'transport_tram': 0.4,
    'recycle_always': -0.2,
    'recycle_sometimes': -0.1,
    'recycle_never': 0,
    'heating_gas': 3,
    'heating_electricity': 2.5,
    'heating_wood_coal': 4,
    'heating_central': 2,
    'flights_more_than_3': 1000 / 365,  
    'flights_1_3': 500 / 365,
    'flights_few_years': 100 / 365,
    'flights_never': 0,
    'public_transport_yes': 1.8,
    'public_transport_no': 0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    total_emissions = 0  
    q1 = None
    q2 = []
    q3 = None
    q4 = None
    q5 = None

    if request.method == 'POST':
        # Регулярное использование общественного транспорта
        q1 = request.form.get('q1')
        if q1 == 'yes':
            total_emissions += emission_factors['public_transport_yes']
        else:
            total_emissions += emission_factors['public_transport_no']

        # Виды транспорта
        q2 = request.form.getlist('q2[]') 
        for transport in q2:
            if transport == 'car':
                total_emissions += emission_factors['transport_car']
            elif transport == 'bus':
                total_emissions += emission_factors['transport_bus']
            elif transport == 'metro':
                total_emissions += emission_factors['transport_metro']
            elif transport == 'motorcycle':
                total_emissions += emission_factors['transport_motorcycle']
            elif transport == 'train':
                total_emissions += emission_factors['transport_train']
            elif transport == 'tram':
                total_emissions += emission_factors['transport_tram']

        # Переработка отходов
        q3 = request.form.get('q3')
        if q3 == 'always':
            total_emissions += emission_factors['recycle_always']
        elif q3 == 'sometimes':
            total_emissions += emission_factors['recycle_sometimes']
        else:
            total_emissions += emission_factors['recycle_never']

        # Авиаперелеты
        q4 = request.form.get('q4')
        if q4 == 'more than 3 times a year':
            total_emissions += emission_factors['flights_more_than_3']
        elif q4 == '1-3 times a year':
            total_emissions += emission_factors['flights_1_3']
        elif q4 == 'once every few years':
            total_emissions += emission_factors['flights_few_years']
        else:
            total_emissions += emission_factors['flights_never']

        # Тип отопления
        q5 = request.form.get('q5')
        if q5 == 'gas':
            total_emissions += emission_factors['heating_gas']
        elif q5 == 'electricity':
            total_emissions += emission_factors['heating_electricity']
        elif q5 == 'wood/coal':
            total_emissions += emission_factors['heating_wood_coal']
        else:
            total_emissions += emission_factors['heating_central']

    return render_template('fixed_index.html', total_emissions=total_emissions, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)

if __name__ == "__main__":
    app.run(debug=True)