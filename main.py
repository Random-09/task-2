"""Задача на 10 баллов"""
from app_setup import app, render_template, request


@app.route('/', methods=['GET', 'POST'])
def main():
    numbers = request.form.get('numbers')
    reversed_numbers = []
    if numbers is not None:
        reversed_numbers = [(num, round(1 / float(num), 2)) for num in numbers.split()]
    return render_template('main.html', reversed_numbers=reversed_numbers)


if __name__ == '__main__':
    app.run()